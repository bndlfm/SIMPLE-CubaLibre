import random

class Government():
    def __init__(self, id):
        self.id = id
        self.color = 'blue'
        self.score = 0
        self.hand = Hand()
        self.position = Position()

class Directorio():
    def __init__(self, id):
        self.id = id
        self.color = 'yellow'
        self.score = 0
        self.hand = Hand()
        self.position = Position()

class July26():
    def __init__(self, id):
        self.id = id
        self.color = 'red'
        self.score = 0
        self.hand = Hand()
        self.position = Position()

class Syndicate():
    def __init__(self, id):
        self.id = id
        self.color = 'green'
        self.score = 0
        self.hand = Hand()
        self.position = Position()


cards = [
    Card(1, "Armored Cars", "GMDS", {
        "unshaded": "In rebel service: 26July or DR free Marches into a space and free Ambushes there (even if Active).",
        "shaded": "Delivered: Until Propaganda, before Assault, move Troops to Assault spaces from other spaces."
    }, "MOMENTUM"),

    Card(2, "Guantánamo Bay", "GMDS", {
        "unshaded": "Base personnel targeted: 26July may Kidnap in Sierra Maestra as if City.",
        "shaded": "US airfield: Until Propaganda, Air Strike removes 2 pieces and allowed even if Embargoed."
    }, "CAPABILITY"),

    Card(3, "Eulogio Cantillo", "GMSD", {
        "unshaded": "General seals truce: Select a space with Troops. A Faction free Marches all its Guerrillas out, then flips them Underground.",
        "shaded": "Dictator backs general’s offensive: Select a Province or City with Troops. They free Sweep in place, then free Assault."
    }),

    Card(4, "S.I.M.", "GMSD", {
        "unshaded": "Word of torture: Remove Support from a space with no Police.",
        "shaded": "Military intelligence gleans leads: Until next Propaganda, Police Sweep and Assault as if Troops."
    }, "MOMENTUM"),

    Card(5, "Rolando Masferrer", "GDMS", {
        "unshaded": "Brutal commander: Set a Province with Troops and 1 adjacent Province to Passive Opposition.",
        "shaded": "Paramilitaries: Sweep may free Assault 1 space as its Special Activity (until Propaganda)."
    }, "MOMENTUM"),

    Card(6, "Sánchez Mosquera", "GDMS", {
        "unshaded": "Popular colonel wounded: Remove all Troops from a Mountain space (to available).",
        "shaded": "Effective army commander: Until next Propaganda, Assault treats Mountain as City."
    }, "MOMENTUM"),

    Card(7, "Election", "GDSM", {
        "unshaded": "Postponed! Rebel ranks grow: Place 1 Guerrilla in each City.",
        "shaded": "Scheduled! Batista bows to US pressure: Set a City to Neutral. Aid +10"
    }),

    Card(8, "General Strike", "GDSM", {
        "unshaded": "Widespread disruption: In each City, shift 1 level toward Neutral and place any 1 Guerrilla.",
        "shaded": "Strike fails, shops open: Set a City to Active Support and Activate all Guerrillas there. Open any 1 closed Casino."
    }),

    Card(9, "Coup", "GSMD", {
        "unshaded": "Batista ousted!: Shift all Govt Control spaces 1 level toward Neutral. US Alliance up 1 box.",
        "shaded": "US-backed plot discovered: Activate and free Assault all DR pieces in Cities with cubes. US Alliance down 1 box."
    }),

    Card(10, "MAP", "GSMD", {
        "unshaded": "Arms shipment stolen: Replace a cube with any 2 Guerrillas.",
        "shaded": "US training: Until Propaganda, Govt may accompany LimOps with a free Special Activity."
    }, "MOMENTUM"),

    Card(11, "Batista Flees", "GSDM", {
        "unshaded": "US forces dictator out: Government Resources –10. Select and remove a die roll of Troops. US Alliance 1 box up. Aid +10. Government Redeploys as in Propaganda round."
    }),

    Card(12, "BRAC", "GSDM", {
        "unshaded": "Anti-subversion agency: Remove any 2 Guerrillas.",
        "shaded": "CIA trains political police: Place 1 Police anywhere. Add lesser of +6 or Aid to Government Resources."
    }),

    Card(13, "El Che", "MGDS", {
        "unshaded": "Inspired military leader: The first group of Guerrillas to move on each 26July March operation flips Underground"
    }, "CAPABILITY"),

    Card(14, "Operation Fisherman", "MGDS", {
        "unshaded": "2nd invasion: Place a 26July Base and Guerrilla in Pinar del Río.",
        "shaded": "Locals resent being drawn in: Shift Pinar del Río 2 levels toward Active Support."
    }),

    Card(15, "Come Comrades!", "MGSD", {
        "unshaded": "Communist recruits: Place 3 26July Guerrillas anywhere.",
        "shaded": "Soviet influence suspected: Add lesser of Aid or +10 to Government Resources. Then Aid +5."
    }),

    Card(16, "Larrazábal", "MGSD", {
        "unshaded": "Venezuelan junta supplies arms: Place a 26July Base where there is a 26July piece.",
        "shaded": "Caracas cuts off shipments: Remove one 26July Base. 26July Resources –3."
    }),

    Card(17, "Alberto Bayo", "MDGS", {
        "unshaded": "Vet trains guerrillas: 26July or DR free Rallies in each space it has a Base (as if spaces Neutral).",
        "shaded": "Mexico blocks training by Cuban expat: All 26July Guerrillas Active. 26July Ineligible through next card."
    }),

    Card(18, "Pact of Caracas", "MDGS", {
        "unshaded": "INSURGENT CAPABILITY: No 26July or DR Ops or Special Activities that remove the other’s pieces or affect placed Opposition. If same player, mutual transfers allowed. If either removes 2 of its Bases at once, cancel Capability. Executing Faction stays Eligible for next card.",
        "shaded": "The 1958 Pact of Caracas was an important agreement that united all insurgents fighting against Batista, setting aside their differences in order to work together toward the overthrow of the dictator. The Pact essentially papered over fundamental differences in visions for the future of Cuba."
    }, "CAPABILITY"),

    Card(19, "Sierra Maestra Manifesto", "MDSG", {
        "unshaded": "Fidel disdains elections or compromise: In card Faction order, each Faction may place 2 non-Casino pieces in a space where they already have a piece. Executing Faction stays Eligible.",
        "shaded": "The Manifesto rejected any political compromise and committed the insurgents the overthrow of the government. Essentially an escalation of the conflict, it may have also been Fidel’s best piece of rhetoric."
    }),

    Card(20, "The Twelve", "MDSG", {
        "unshaded": "Tale of survivors inspires movement: A Faction free Marches then free Rallies at a March destination.",
        "shaded": "Granma travail presages supply challenge: Remove 1/2 rounded up of any Guerrillas from the space with the most Guerrillas."
    }),

    Card(21, "Fangio", "MSGD", {
        "unshaded": "26July seizes racer: Shift a City 1 level toward Active Opposition, 2 levels if a 26July piece is there.",
        "shaded": "Famous driver popularizes Cuba: In 2 spaces with any Casinos, open a closed Casino or place 1 Cash with a Guerrilla or cube."
    }),

    Card(22, "Raúl", "MSGD", {
        "unshaded": "INSURGENT CAPABILITY: Younger Castro an ace: 26July may reroll each Attack or Kidnap.",
        "shaded": "GOVERNMENT MOMENTUM: US hostage-taking backfires: Until Propaganda, add to Aid twice any Resources from Kidnap."
    }),

    Card(23, "Radio Rebelde", "MSDG", {
        "unshaded": "Clandestine radio reaches masses: Shift 2 Provinces each 1 level toward Active Opposition.",
        "shaded": "Transmitter pinpointed: Remove a 26July Base from a Province."
    }),

    Card(24, "Vilma Espín", "MSDG", {
        "unshaded": "Revolutionary interlocutor: Set Sierra Maestra or an adjacent space to Active Opposition.",
        "shaded": "Raúl’s fiancé betrays urban guerrilla: Remove all 26July pieces from a City other than Havana."
    }),

    Card(25, "Escapade", "DGMS", {
        "unshaded": "Yacht brings fighters: Place a DR Guerrilla and Base in either Camagüey Province or Oriente.",
        "shaded": "Resupply yacht intercepted: Remove a Directorio Base."
    }),

    Card(26, "Rodríguez Loeches", "DGMS", {
        "unshaded": "DR Leader: DR places 1 Guerrilla anywhere and free Marches to, Rallies, or Ambushes there.",
        "shaded": "Inefficient administrator: Remove 1 DR Guerrilla. DR Resources –5."
    }),

    Card(27, "Echeverría", "DGSM", {
        "unshaded": "Near-miss attempt on dictator’s life: Place 2 DR Guerrillas anywhere. Havana to Neutral. DR to Eligible.",
        "shaded": "Popular revolutionary dies in his “hit at the top”: Remove the 2 DR pieces closest to Havana. DR Resources –3."
    }),

    Card(28, "Morgan", "DGSM", {
        "unshaded": "INSURGENT CAPABILITY: US Comandante: DR Guerrillas may March 2 adjacent spaces.",
        "shaded": "Backlash against Yanqui adventurer: Set a space with a DR Guerrilla to Active Support."
    }),

    Card(29, "Fauré Chomón", "DMGS", {
        "unshaded": "Students take to the field: DR or 26July places a Base and 2 Guerrillas in Las Villas.",
        "shaded": "Student loyalties shift: Remove a DR piece or replace it with its 26July counterpart."
    }),

    Card(30, "The Guerrilla Life", "DMGS", {
        "unshaded": "INSURGENT CAPABILITY: Hardships harden 26July fighters: All 26July Rallies flip Guerrillas Underground, even if placing.",
        "shaded": "Hardships harden student revolutionaries: Flip all DR Guerrillas Underground. Place 1 DR Guerrilla in a City."
    }),

    Card(31, "Escopeteros", "DMSG", {
        "unshaded": "Locals start their own revolution: Place any non-Casino Base and any 1 Guerrilla into a Mountain.",
        "shaded": "Traditionalist countryside rejects rebellion: Shift a Mountain space 1 level toward Active Support."
    }),

    Card(32, "Resistencia Cívica", "DMSG", {
        "unshaded": "Urban movement backs Castro: In a City, replace all Directorio pieces with 26July counterparts.",
        "shaded": "Movement splits with Castro: In a City, replace all 26July pieces with Directorio counterparts."
    }),

    Card(33, "Carlos Prío", "DSGM", {
        "unshaded": "Ex-president funnels funds: +5 DR or +5 26July Resources.",
        "shaded": "Return from exile: Select a space without Govt Control. Place a DR Base there and set it to Neutral."
    }),

    Card(34, "US Speaking Tour", "DSGM", {
        "unshaded": "Expatriates invest: An Insurgent Faction adds a die roll in Resources. Each other adds +2.",
        "shaded": "An embarrassment: Add the lesser of +8 or Aid to Government Resources. Then Aid +8."
    }),

    Card(35, "Defections", "DSMG", {
        "unshaded": "Disillusioned fighters: In a space already occupied by your pieces and those of an enemy, replace 2 of the enemy’s Guerrillas or cubes with your Guerrillas or cubes.",
        "shaded": "Every faction in the conflict suffered from defections, including the Syndicate, which lost employees to the insurgency and to the Government. More valuable than the manpower was the intelligence gained from these defections."
    }),

    Card(36, "Eloy Gutiérrez Menoyo", "DSMG", {
        "unshaded": "Inspiring DR leader: Replace a non-DR non-Casino piece within 1 space of Las Villas with 2 DR Guerrillas.",
        "shaded": "Commander fractious: Replace a Directorio Guerrilla with a non-Directorio Guerrilla."
    }),

    Card(37, "Herbert Matthews", "SGMD", {
        "unshaded": "NYTimes refutes Fidel’s death: 26July Resources +5. Aid -6.",
        "shaded": "Fidel’s survival spurs support to counterweights: Aid +10. Directorio Resources +3. Syndicate Resources +5."
    }),

    Card(38, "Meyer Lansky", "SGMD", {
        "unshaded": "Wheeler dealer: Within a space, transfer any Cash among any Guerrillas or cubes.",
        "shaded": "Master mobster: Syndicate relocates any Casinos anywhere (within stacking). All Casinos open."
    }),

    Card(39, "Turismo", "SGDM", {
        "unshaded": "“Ugly American”: Support 1 level toward Neutral each Casino space.",
        "shaded": "Police “protection” for tourists: Govt and Syndicate each add +3 Resources per space with open Casino and Police"
    }),

    Card(40, "Ambassador Smith", "SGDM", {
        "unshaded": "Havana advocate ignored in US: Shift US Alliance 1 box down (leave Aid the same).",
        "shaded": "Blindly backing dictator: Shift US Alliance 1 box up. Aid +9. Then add lesser of +9 or half Aid (round down) to Syndicate Resources."
    }),

    Card(41, "Fat Butcher", "SMGD", {
        "unshaded": "Casino-man Nicholas di Costanzo draws US heat: Close 1 Casino or reduce Aid -8.",
        "shaded": "Mob enforcer: Syndicate free Ambushes with 1 of its Underground Guerrillas and opens 1 closed Casino."
    }),

    Card(42, "Llano", "SMGD", {
        "unshaded": "Slums to arms: Place a 26July Base and any Guerrilla in a City.",
        "shaded": "Urban poor indifferent, eager for work: Select a City. Remove any Opposition there and place an open Casino"
    }),

    Card(43, "Mafia Offensive", "SMDG", {
        "unshaded": "Mob helps rebels: 26July or DR executes a free LimOp, treating 1 Syndicate piece as that Faction’s piece.",
        "shaded": "INSURGENT CAPABILITY: Hitmen: Syndicate may Assassinate as if DR, but regardless of Police."
    }),

    Card(44, "Rebel Air Force", "SMDG", {
        "unshaded": "Captured aircraft shocks troops: A 26July or DR Guerrilla (Active or not) free Ambushes Government forces. Remove Bases first.",
        "shaded": "Rebels purchase but cannot operate aircraft: Select 26July or DR and transfer 1 die roll of their Resources to Syndicate."
    }),

    Card(45, "Anastasia", "SDGM", {
        "unshaded": "Rival muscles into Cuba: Close all Casinos in Havana. Syndicate Resources -5.",
        "shaded": "Lansky rival whacked in New York: Syndicate Resources +10."
    }),

    Card(46, "Sinatra", "SDGM", {
        "unshaded": "Over-priced star: Syndicate Resources -6.",
        "shaded": "Frankie’s show: Place an open Casino in Havana regardless of stacking. Place 1 Cash with Police there."
    }),

    Card(47, "Pact of Miami", "SDMG", {
        "unshaded": "Surprise for dictator and rebels: Remove 2 Guerrillas. Govt Ineligible through next card.",
        "shaded": "Agreement causes confusion: 26July and Directorio each lose –3 Resources and are Ineligible through next card."
    }),

    Card(48, "Santo Trafficante, Jr", "SDMG", {
        "unshaded": "Feud with Lansky: Syndicate Resources –10. All Syndicate Guerrillas to Active.",
        "shaded": "INSURGENT CAPABILITY: Old-time mobster: Any Underground Syndicate Guerrillas block Skim (6.2.3)."
    },"CAPABILITY"),
]
        
       
#TODO: Haven't looked at from here to EOF
class Deck():
    def __init__(self, contents):
        self.contents = contents
        self.create()
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n):
        drawn = []
        for x in range(n):
            drawn.append(self.cards.pop())
        return drawn
    
    def add(self, cards):
        for card in cards:
            self.cards.append(card)

    def create(self):
        self.cards = []

        card_id = 0
        for order, x in enumerate(self.contents):
            x['info']['order'] = order
            for i in range(x['count']):
                x['info']['id'] = card_id
                self.add([x['card'](**x['info'])])
                card_id += 1
                
        self.shuffle()
                
    def size(self):
        return len(self.cards)


class Hand():
    def __init__(self):
        self.cards = []  
    
    def add(self, cards):
        for card in cards:
            self.cards.append(card)
    
    def size(self):
        return len(self.cards)
    
    def pick(self, name):
        for i, c in enumerate(self.cards):
            if c.name == name:
                self.cards.pop(i)
                return c
        
                
class Discard():
    def __init__(self):
        self.cards = []  
    
    def add(self, cards):
        for card in cards:
            self.cards.append(card)
    
    def size(self):
        return len(self.cards)
    
class Position():
    def __init__(self):
        self.cards = []  
    
    def add(self, cards):
        for card in cards:
            self.cards.append(card)
    
    def size(self):
        return len(self.cards)

    def pick(self, name):
        for i, c in enumerate(self.cards):
            if c.name == name:
                self.cards.pop(i)
                return c
