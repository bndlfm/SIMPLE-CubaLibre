import random

from typing import List

from gym.envs.registration import register
from gym import spaces


class CubaLibreEnv:                 #{{{ TODO:
    def __init__(self):             #{{{ TODO:
        self.action_space = spaces.Discrete(2)  # 0: Move to discard, 1: Reveal new card
        self.observation_space = spaces.Discrete(len(self.deck) + 1)  # Number of cards + 1 for the discard pile

        # Initialize game state
        self.reset()            
    #}}}

    def reset(self):                #{{{ TODO:
        """Reset the game to its initial state."""
        propaganda_cards = [PropagandaCard(id=i, name=f"PropagandaCard {i}") for i in range(1, 4)]
        self.deck = prepare_deck(event_cards, propaganda_cards)

        # Create 5 instances of PropagandaCard and add them to the cards list
        for i in range(5):
            cards.append(PropagandaCard(id=len(cards) + 1, name=f"PropagandaCard {i + 1}"))
        random.shuffle(self.deck)

        self.discard_pile = []
        self.revealed_card = self.deck.pop()

        return self.get_observation()
    #}}}

    def step(self, action):         #{{{ TODO:
        """Execute the chosen action and update the game state."""
        reward = 0

        # Check the current event card (top card of the discard pile)
        current_event_card = self.discard_pile[-1] if self.discard_pile else None
        revealed_event_card = self.deck[-1] if self.deck else None

        # Determine the eligible factions for the current event card
        eligible_factions = self.get_eligible_factions(current_event_card)

        # Allow the agent to choose an action based on the eligible factions and the current event card
        chosen_action, chosen_faction = self.choose_action(action, eligible_factions, current_event_card)

        # Execute the chosen action
        self.execute_action(chosen_action, chosen_faction, current_event_card)

        # Determine the reward based on the chosen action
        reward = self.get_reward(chosen_action, chosen_faction, current_event_card)

        # Move the revealed card to the discard pile, making it the current event card for the next turn
        if self.deck:
            self.discard_pile.append(self.deck.pop())

        # Check for end of game or other conditions
        done = len(self.deck) == 0
        return self.get_observation(), reward, done, {}
    #}}}

    def get_revealed_card(self):    #{{{ TODO:
        """Get the top card of the deck (revealed card for the next turn)."""
        return self.deck[-1] if self.deck else None
    #}}}

    def get_observation(self):      #{{{ TODO:
        """Return the current game state."""
        # This can be expanded based on what you want the agent to observe
        return len(self.discard_pile)
    #}}}

    def render(self, mode='human'): #{{{ TODO:
        """Display the current game state."""
        print(f"Revealed Card: {self.revealed_card.name}")
        print(f"Discard Pile: {[card.name for card in self.discard_pile]}")
    #}}}

    register(
        id='CubaLibre-v0',
        entry_point='your_module_name:CubaLibreEnv',
    )
#}}}

class Faction:                      #{{{
    def __init__(self, faction_id, color, score, income):
        self.id = faction_id
        self.color = color
        self.score = score
        self.income = income

class Government(Faction):
    def __init__(self, faction_id, color, score, income):
        super().__init__(faction_id, color, score, income)
        self.id = "gov"
        self.color = 'blue'
        self.score = 0
        self.income = 0

class Directorio(Faction):
    def __init__(self, faction_id, color, score, income):
        super().__init__(faction_id, color, score, income)
        self.id = "gov"
        self.color = 'blue'
        self.score = 0
        self.income = 0

class July26(Faction):
    def __init__(self, faction_id, color, score, income):
        super().__init__(faction_id, color, score, income)
        self.id = "gov"
        self.color = 'blue'
        self.score = 0
        self.income = 0

class Syndicate(Faction):
    def __init__(self, faction_id, color, score, income):
        super().__init__(faction_id, color, score, income)
        self.id = "gov"
        self.color = 'blue'
        self.score = 0
        self.income = 0
#}}}

class Card:                         #{{{ TODO:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def execute(self):
        pass
    #}}}

class EventCard(Card):              #{{{ TODO:
    def __init__(self, id, name, faction_order, unshaded_txt, unshaded_cap, shaded_txt, shaded_cap):
        super().__init__(id, name)
        self.eligibility = faction_order  # List of factions in order of execution
        self.unshaded = unshaded_txt
        self.unshaded.cap = unshaded_cap
        self.shaded = shaded_txt
        self.shaded.cap = shaded_cap
    def execute(self, faction):
        # TODO: Logic to execute the event based on the faction
        pass

# Event Cards Instantiation     #{{{
event_cards: List[EventCard] = [
    EventCard(1, "Armored Cars", "GMDS",
        "In rebel service: 26July or DR free Marches into a space and free Ambushes there (even if Active).", False,
        "Delivered: Until Propaganda, before Assault, move Troops to Assault spaces from other spaces.", False,
    ),
    EventCard(2, "Guantánamo Bay", "GMDS",
		"Base personnel targeted: 26July may Kidnap in Sierra Maestra as if City.", False,
		"US airfield: Until Propaganda, Air Strike removes 2 pieces and allowed even if Embargoed.", False,
	),
    EventCard(3, "Eulogio Cantillo", "GMSD",
		"General seals truce: Select a space with Troops. A Faction free Marches all its Guerrillas out, then flips them Underground.", False,
		"Dictator backs general’s offensive: Select a Province or City with Troops. They free Sweep in place, then free Assault.", False,
	),
    EventCard(4, "S.I.M.", "GMSD",
		"Word of torture: Remove Support from a space with no Police.", False,
		"Military intelligence gleans leads: Until next Propaganda, Police Sweep and Assault as if Troops.", False,
	),
    EventCard(5, "Rolando Masferrer", "GDMS",
		"Brutal commander: Set a Province with Troops and 1 adjacent Province to Passive Opposition.", False,
		"Paramilitaries: Sweep may free Assault 1 space as its Special Activity (until Propaganda).", False,
	),
    EventCard(6, "Sánchez Mosquera", "GDMS",
		"Popular colonel wounded: Remove all Troops from a Mountain space (to available).", False,
		"Effective army commander: Until next Propaganda, Assault treats Mountain as City.", False,
	),
    EventCard(7, "Election", "GDSM",
		"Postponed! Rebel ranks grow: Place 1 Guerrilla in each City.", False,
		"Scheduled! Batista bows to US pressure: Set a City to Neutral. Aid +10", False,
	),
    EventCard(8, "General Strike", "GDSM",
		"Widespread disruption: In each City, shift 1 level toward Neutral and place any 1 Guerrilla.", False,
		"Strike fails, shops open: Set a City to Active Support and Activate all Guerrillas there. Open any 1 closed Casino.", False,
	),
    EventCard(9, "Coup", "GSMD",
		"Batista ousted!: Shift all Govt Control spaces 1 level toward Neutral. US Alliance up 1 box.", False,
		"US-backed plot discovered: Activate and free Assault all DR pieces in Cities with cubes. US Alliance down 1 box.", False,
	),
    EventCard(10, "MAP", "GSMD",
		"Arms shipment stolen: Replace a cube with any 2 Guerrillas.", False,
		"US training: Until Propaganda, Govt may accompany LimOps with a free Special Activity.", False,
	),
    EventCard(11, "Batista Flees", "GSDM",
        "US forces dictator out: Government Resources –10. Select and remove a die roll of Troops. US Alliance 1 box up. Aid +10. Government Redeploys as in Propaganda round.", False,
        "", False,
    ),
    EventCard(12, "BRAC", "GSDM",
		"Anti-subversion agency: Remove any 2 Guerrillas.", False,
		"CIA trains political police: Place 1 Police anywhere. Add lesser of +6 or Aid to Government Resources.", False,
	),
    EventCard(13, "El Che", "MGDS",
        "Inspired military leader: The first group of Guerrillas to move on each 26July March operation flips Underground", True,
        "", False,
    ),
    EventCard(14, "Operation Fisherman", "MGDS",
		"2nd invasion: Place a 26July Base and Guerrilla in Pinar del Río.", False,
		"Locals resent being drawn in: Shift Pinar del Río 2 levels toward Active Support.", False,
	),
    EventCard(15, "Come Comrades!", "MGSD",
		"Communist recruits: Place 3 26July Guerrillas anywhere.", False,
		"Soviet influence suspected: Add lesser of Aid or +10 to Government Resources. Then Aid +5.", False,
	),
    EventCard(16, "Larrazábal", "MGSD",
		"Venezuelan junta supplies arms: Place a 26July Base where there is a 26July piece.", False,
		"Caracas cuts off shipments: Remove one 26July Base. 26July Resources –3.", False,
	),
    EventCard(17, "Alberto Bayo", "MDGS",
		"Vet trains guerrillas: 26July or DR free Rallies in each space it has a Base (as if spaces Neutral).", False,
		"Mexico blocks training by Cuban expat: All 26July Guerrillas Active. 26July Ineligible through next card.", False,
	),
    EventCard(18, "Pact of Caracas", "MDGS",
		"INSURGENT CAPABILITY: No 26July or DR Ops or Special Activities that remove the other’s pieces or affect placed Opposition. If same player, mutual transfers allowed. If either removes 2 of its Bases at once, cancel Capability. Executing Faction stays Eligible for next card.", False,
		"", False,
	),
    EventCard(19, "Sierra Maestra Manifesto", "MDSG",
		"Fidel disdains elections or compromise: In card Faction order, each Faction may place 2 non-Casino pieces in a space where they already have a piece. Executing Faction stays Eligible.", False,
		"The Manifesto rejected any political compromise and committed the insurgents the overthrow of the government. Essentially an escalation of the conflict, it may have also been Fidel’s best piece of rhetoric.", False,
	),
    EventCard(20, "The Twelve", "MDSG",
		"Tale of survivors inspires movement: A Faction free Marches then free Rallies at a March destination.", False,
		"Granma travail presages supply challenge: Remove 1/2 rounded up of any Guerrillas from the space with the most Guerrillas.", False,
	),
    EventCard(21, "Fangio", "MSGD",
		"26July seizes racer: Shift a City 1 level toward Active Opposition, 2 levels if a 26July piece is there.", False,
		"Famous driver popularizes Cuba: In 2 spaces with any Casinos, open a closed Casino or place 1 Cash with a Guerrilla or cube.", False,
	),
    EventCard(22, "Raúl", "MSGD",
		"INSURGENT CAPABILITY: Younger Castro an ace: 26July may reroll each Attack or Kidnap.", False,
		"GOVERNMENT MOMENTUM: US hostage-taking backfires: Until Propaganda, add to Aid twice any Resources from Kidnap.", False,
	),
    EventCard(23, "Radio Rebelde", "MSDG",
		"Clandestine radio reaches masses: Shift 2 Provinces each 1 level toward Active Opposition.", False,
		"Transmitter pinpointed: Remove a 26July Base from a Province.", False,
	),
    EventCard(24, "Vilma Espín", "MSDG",
		"Revolutionary interlocutor: Set Sierra Maestra or an adjacent space to Active Opposition.", False,
		"Raúl’s fiancé betrays urban guerrilla: Remove all 26July pieces from a City other than Havana.", False,
	),
    EventCard(25, "Escapade", "DGMS",
		"Yacht brings fighters: Place a DR Guerrilla and Base in either Camagüey Province or Oriente.", False,
		"Resupply yacht intercepted: Remove a Directorio Base.", False,
	),
    EventCard(26, "Rodríguez Loeches", "DGMS",
		"DR Leader: DR places 1 Guerrilla anywhere and free Marches to, Rallies, or Ambushes there.", False,
		"Inefficient administrator: Remove 1 DR Guerrilla. DR Resources –5.", False,
	),
    EventCard(27, "Echeverría", "DGSM",
		"Near-miss attempt on dictator’s life: Place 2 DR Guerrillas anywhere. Havana to Neutral. DR to Eligible.", False,
		"Popular revolutionary dies in his “hit at the top”: Remove the 2 DR pieces closest to Havana. DR Resources –3.", False,
	),
    EventCard(28, "Morgan", "DGSM",
		"INSURGENT CAPABILITY: US Comandante: DR Guerrillas may March 2 adjacent spaces.", False,
		"Backlash against Yanqui adventurer: Set a space with a DR Guerrilla to Active Support.", False,
	),
    EventCard(29, "Fauré Chomón", "DMGS",
		"Students take to the field: DR or 26July places a Base and 2 Guerrillas in Las Villas.", False,
		"Student loyalties shift: Remove a DR piece or replace it with its 26July counterpart.", False,
	),
    EventCard(30, "The Guerrilla Life", "DMGS",
		"INSURGENT CAPABILITY: Hardships harden 26July fighters: All 26July Rallies flip Guerrillas Underground, even if placing.", False,
		"Hardships harden student revolutionaries: Flip all DR Guerrillas Underground. Place 1 DR Guerrilla in a City.", False,
	),
    EventCard(31, "Escopeteros", "DMSG",
		"Locals start their own revolution: Place any non-Casino Base and any 1 Guerrilla into a Mountain.", False,
		"Traditionalist countryside rejects rebellion: Shift a Mountain space 1 level toward Active Support.", False,
	),
    EventCard(32, "Resistencia Cívica", "DMSG",
		"Urban movement backs Castro: In a City, replace all Directorio pieces with 26July counterparts.", False,
		"Movement splits with Castro: In a City, replace all 26July pieces with Directorio counterparts.", False,
	),
    EventCard(33, "Carlos Prío", "DSGM",
		"Ex-president funnels funds: +5 DR or +5 26July Resources.", False,
		"Return from exile: Select a space without Govt Control. Place a DR Base there and set it to Neutral.", False,
	),
    EventCard(34, "US Speaking Tour", "DSGM",
		"Expatriates invest: An Insurgent Faction adds a die roll in Resources. Each other adds +2.", False,
		"An embarrassment: Add the lesser of +8 or Aid to Government Resources. Then Aid +8.", False,
	),
    EventCard(35, "Defections", "DSMG",
		"Disillusioned fighters: In a space already occupied by your pieces and those of an enemy, replace 2 of the enemy’s Guerrillas or cubes with your Guerrillas or cubes.", False,
		"Every faction in the conflict suffered from defections, including the Syndicate, which lost employees to the insurgency and to the Government. More valuable than the manpower was the intelligence gained from these defections.", False,
	),
    EventCard(36, "Eloy Gutiérrez Menoyo", "DSMG",
		"Inspiring DR leader: Replace a non-DR non-Casino piece within 1 space of Las Villas with 2 DR Guerrillas.", False,
		"Commander fractious: Replace a Directorio Guerrilla with a non-Directorio Guerrilla.", False,
	),
    EventCard(37, "Herbert Matthews", "SGMD",
		"NYTimes refutes Fidel’s death: 26July Resources +5. Aid -6.", False,
		"Fidel’s survival spurs support to counterweights: Aid +10. Directorio Resources +3. Syndicate Resources +5.", False,
	),
    EventCard(38, "Meyer Lansky", "SGMD",
		"Wheeler dealer: Within a space, transfer any Cash among any Guerrillas or cubes.", False,
		"Master mobster: Syndicate relocates any Casinos anywhere (within stacking). All Casinos open.", False,
	),
    EventCard(39, "Turismo", "SGDM",
		"“Ugly American”: Support 1 level toward Neutral each Casino space.", False,
		"Police “protection” for tourists: Govt and Syndicate each add +3 Resources per space with open Casino and Police", False,
	),
    EventCard(40, "Ambassador Smith", "SGDM",
		"Havana advocate ignored in US: Shift US Alliance 1 box down (leave Aid the same).", False,
		"Blindly backing dictator: Shift US Alliance 1 box up. Aid +9. Then add lesser of +9 or half Aid (round down) to Syndicate Resources.", False,
	),
    EventCard(41, "Fat Butcher", "SMGD",
		"Casino-man Nicholas di Costanzo draws US heat: Close 1 Casino or reduce Aid -8.", False,
		"Mob enforcer: Syndicate free Ambushes with 1 of its Underground Guerrillas and opens 1 closed Casino.", False,
	),
    EventCard(42, "Llano", "SMGD",
		"Slums to arms: Place a 26July Base and any Guerrilla in a City.", False,
		"Urban poor indifferent, eager for work: Select a City. Remove any Opposition there and place an open Casino", False,
	),
    EventCard(43, "Mafia Offensive", "SMDG",
		"Mob helps rebels: 26July or DR executes a free LimOp, treating 1 Syndicate piece as that Faction’s piece.", False,
		"INSURGENT CAPABILITY: Hitmen: Syndicate may Assassinate as if DR, but regardless of Police.", False,
	),
    EventCard(44, "Rebel Air Force", "SMDG",
		"Captured aircraft shocks troops: A 26July or DR Guerrilla (Active or not) free Ambushes Government forces. Remove Bases first.", False,
		"Rebels purchase but cannot operate aircraft: Select 26July or DR and transfer 1 die roll of their Resources to Syndicate.", False,
	),
    EventCard(45, "Anastasia", "SDGM",
		"Rival muscles into Cuba: Close all Casinos in Havana. Syndicate Resources -5.", False,
		"Lansky rival whacked in New York: Syndicate Resources +10.", False,
	),
    EventCard(46, "Sinatra", "SDGM",
		"Over-priced star: Syndicate Resources -6.", False,
		"Frankie’s show: Place an open Casino in Havana regardless of stacking. Place 1 Cash with Police there.", False,
	),
    EventCard(47, "Pact of Miami", "SDMG",
		"Surprise for dictator and rebels: Remove 2 Guerrillas. Govt Ineligible through next card.", False,
		"Agreement causes confusion: 26July and Directorio each lose –3 Resources and are Ineligible through next card.", False,
	),
    EventCard(48, "Santo Trafficante, Jr", "SDMG",
		"Feud with Lansky: Syndicate Resources –10. All Syndicate Guerrillas to Active.", False,
		"INSURGENT CAPABILITY: Old-time mobster: Any Underground Syndicate Guerrillas block Skim (6.2.3).", False,
	),
] #}}} }}}

class PropagandaCard(Card):         #{{{ TODO:
    def __init__(self, id, name):
        super().__init__(id, name)
    def execute(self):
        # TODO: Logic to conduct a Propaganda Round
        pass 
#}}} }}}


#-------- def prepare_deck -------- #{{{
def prepare_deck(event_cards: list, propaganda_cards: list) -> list:
    """
    Prepare the game deck based on the given instructions.

    Args:
    - event_cards (list): List of all event cards.
    - propaganda_cards (list): List of all propaganda cards.

    Returns:
    - list: Prepared game deck.
    """

    # Shuffle the event cards
    random.shuffle(event_cards)

    # Split the event cards into 4 roughly equal piles
    split_size = len(event_cards) // 4
    piles = [event_cards[i:i+split_size] for i in range(0, len(event_cards), split_size)]

    # Shuffle 1 propaganda card into each pile
    for i in range(4):
        piles[i].append(propaganda_cards[i])
        random.shuffle(piles[i])

    # Stack the piles to form the deck
    deck = []
    for pile in piles:
        deck.extend(pile)

    return deck
#}}}


