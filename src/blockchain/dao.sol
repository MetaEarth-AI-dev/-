// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title METAERTH DAO Contract
 * @dev A decentralized governance system for $METAERTH token holders.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetaEarthDAO is Ownable {
    IERC20 public metaEarthToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    uint256 public proposalCount;
    uint256 public votingPeriod; // Duration of the voting period in seconds
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    event ProposalCreated(uint256 indexed id, address indexed proposer, string description, uint256 startTime, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 weight);
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    /**
     * @dev Initializes the DAO contract with the $METAERTH token address and default voting period.
     * @param tokenAddress The address of the $METAERTH token contract.
     * @param initialVotingPeriod The default voting period in seconds.
     */
    constructor(address tokenAddress, uint256 initialVotingPeriod) {
        metaEarthToken = IERC20(tokenAddress);
        votingPeriod = initialVotingPeriod;
    }

    /**
     * @dev Creates a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external {
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + votingPeriod;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            proposer: msg.sender,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            startTime: startTime,
            endTime: endTime,
            executed: false
        });

        emit ProposalCreated(proposalCount, msg.sender, description, startTime, endTime);
        proposalCount++;
    }

    /**
     * @dev Allows $METAERTH token holders to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.startTime, "Voting has not started yet");
        require(block.timestamp <= proposal.endTime, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        uint256 voterBalance = metaEarthToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold $METAERTH tokens to vote");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposal.votesFor += voterBalance;
        } else {
            proposal.votesAgainst += voterBalance;
        }

        emit Voted(proposalId, msg.sender, support, voterBalance);
    }

    /**
     * @dev Executes a proposal if it has enough votes in favor.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting period is not over");
        require(!proposal.executed, "Proposal has already been executed");

        if (proposal.votesFor > proposal.votesAgainst) {
            proposal.executed = true;
            emit ProposalExecuted(proposalId, true);
            // Add additional logic to implement the proposal's decision
        } else {
            emit ProposalExecuted(proposalId, false);
        }
    }

    /**
     * @dev Updates the voting period.
     * @param newVotingPeriod The new voting period in seconds.
     */
    function updateVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        votingPeriod = newVotingPeriod;
    }
}
