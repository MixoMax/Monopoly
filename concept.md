# Classes:

## Player

- Name
- Position
- Money
- Jail y/n
- Jail turns
- symbol

## Street

- Name
- Price
- Rent
- Owner
- House Count
- (image ?)
- color
- 

## 


---

# Main Loop:

- roll dice
    - if third double
        - send player to jail
- move player

- check if player is on street
    - if street is owned by player
        - do nothing
    - elif street is owned by other player
        - pay rent
    - elif street is not owned
        - ask if player wants to buy
            - if yes && player has enough money
                - buy street
                    - subtract money
                    - add street to player
            - if no
                - auction street
    
- check if player is on special field
    - if player is on jail
        - roll 3 times
            - if player rolls double
                - move player
            - if jail turns == 3
                - if player has get out of jail card
                    - remove card
                    - move player
                - else
                    - pay 50
                    - move player
            
    - if player is on free parking
        - give player free parking money
        
    - if player is on go to jail
        - send player to jail
        
    - if player is on start
        - give player 200
    
    - if player is on special field
        - draw card
        - execute card

- check if player has enough money (>0)
- ask player if he wants to buy houses
    - if yes
        - show streets with houses
        - ask player which street he wants to buy houses for
        - ask player how many houses he wants to buy
        - check if player has enough money
        - buy houses
            - subtract money
            - add houses to street
    - if no
        - do nothing



# House Rules:
- Double Money on start
- Free Parking Money
- 1000 cash for pasch of 1