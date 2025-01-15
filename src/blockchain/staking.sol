// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title METAERTH Staking Contract
 * @dev A contract that allows users to stake $METAERTH tokens and earn rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MetaEarthStaking is Ownable {
    using SafeMath for uint256;

    IERC20 public metaEarthToken;

    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    mapping(address => Staker) public stakers;
    uint256 public totalStaked;
    uint256 public rewardRate; // Tokens rewarded per second per staked token

    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event ClaimRewards(address indexed user, uint256 reward);

    /**
     * @dev Constructor initializes the staking contract with the $METAERTH token.
     * @param tokenAddress The address of the $METAERTH token contract.
     * @param initialRewardRate The initial reward rate for staking.
     */
    constructor(address tokenAddress, uint256 initialRewardRate) {
        metaEarthToken = IERC20(tokenAddress);
        rewardRate = initialRewardRate;
    }

    /**
     * @dev Allows a user to stake $METAERTH tokens.
     * @param amount The number of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        metaEarthToken.transferFrom(msg.sender, address(this), amount);
        staker.stakedAmount = staker.stakedAmount.add(amount);
        staker.lastStakeTime = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Stake(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their $METAERTH tokens.
     * @param amount The number of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        _updateRewards(msg.sender);

        staker.stakedAmount = staker.stakedAmount.sub(amount);
        metaEarthToken.transfer(msg.sender, amount);

        totalStaked = totalStaked.sub(amount);

        emit Unstake(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;
        require(reward > 0, "No rewards to claim");

        staker.rewardDebt = 0;
        metaEarthToken.transfer(msg.sender, reward);

        emit ClaimRewards(msg.sender, reward);
    }

    /**
     * @dev Updates the reward debt of a staker.
     * @param user The address of the staker.
     */
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        if (staker.stakedAmount > 0) {
            uint256 timeElapsed = block.timestamp.sub(staker.lastStakeTime);
            uint256 reward = staker.stakedAmount.mul(timeElapsed).mul(rewardRate).div(1e18);
            staker.rewardDebt = staker.rewardDebt.add(reward);
            staker.lastStakeTime = block.timestamp;
        }
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
