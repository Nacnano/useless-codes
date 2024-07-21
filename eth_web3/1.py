ledger = {
  "0x1234567890abcdef": {"ASSET_A": 100, "ASSET_B": 50},
  "0xfedcba9876543210": {"ASSET_A": 50, "ASSET_B": 100}
}
def transfer(sender_address, recipient_address, asset_id, amount):
    # Check if sender and recipient addresses are different
    if sender_address == recipient_address:
        return "Transfer rejected: Sender and recipient addresses are the same."
    
    # Check if asset_id is recognized
    if asset_id not in ledger[sender_address]:
        return "Transfer rejected: Asset ID is not recognized."
    
    # Check if sender has sufficient balance of asset_id
    if ledger[sender_address][asset_id] < amount:
        return "Transfer rejected: Sender does not have sufficient balance."
    
    # Update sender's balance
    ledger[sender_address][asset_id] -= amount
    
    # Update recipient's balance
    if recipient_address not in ledger:
        ledger[recipient_address] = {}
    if asset_id not in ledger[recipient_address]:
        ledger[recipient_address][asset_id] = 0
    ledger[recipient_address][asset_id] += amount
    
    return "Transfer successful."

transfer("0x1234567890abcdef", "0xfedcba9876543210", "ASSET_A", 20)

print(ledger)