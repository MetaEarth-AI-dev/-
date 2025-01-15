// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title METAERTH Token Contract
 * @dev ERC20 implementation for the $METAERTH token used in MetaEarth AI.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetaEarthToken is ERC20, Ownable {
    uint256 private _initialSupply = 10_000_000_000 * 10 ** decimals(); // 10 billion tokens

    constructor() ERC20("MetaEarthToken", "METAERTH") {
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Allows the owner to mint new tokens.
     * @param account The address to receive the minted tokens.
     * @param amount The number of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    /**
     * @dev Allows the owner to burn tokens.
     * @param account The address from which to burn tokens.
     * @param amount The number of tokens to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
