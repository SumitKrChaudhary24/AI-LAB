# Forward Chaining Implementation

class KnowledgeBase:
    def __init__(self):
        self.facts = set()  # Known facts
        self.rules = []     # Rules of inference

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.facts.add(fact)

    def add_rule(self, rule):
        """Add a rule to the knowledge base."""
        self.rules.append(rule)

    def infer(self):
        """Perform forward chaining to infer new facts."""
        new_facts = set()
        while True:
            inferred = False
            for rule in self.rules:
                # Extract antecedents and consequent
                antecedents, consequent = rule
                if all(antecedent in self.facts for antecedent in antecedents) and consequent not in self.facts:
                    new_facts.add(consequent)
                    inferred = True
            if not inferred:
                break
            self.facts.update(new_facts)
        return new_facts


# Initialize knowledge base
kb = KnowledgeBase()

# Add facts
kb.add_fact("American(Robert)")
kb.add_fact("Enemy(A, America)")
kb.add_fact("Owns(A, T1)")
kb.add_fact("Missile(T1)")

# Add rules
kb.add_rule((["Enemy(A, America)"], "Hostile(A)"))  # Hostility rule
kb.add_rule((["Missile(T1)"], "Weapon(T1)"))        # Missiles are weapons
kb.add_rule((["Missile(T1)", "Owns(A, T1)"], "Sells(Robert, T1, A)"))  # Sellers of missiles
kb.add_rule((
    ["American(Robert)", "Weapon(T1)", "Sells(Robert, T1, A)", "Hostile(A)"],
    "Criminal(Robert)"
))  # Crime rule

# Perform inference
kb.infer()

# Check if the goal is proven
goal = "Criminal(Robert)"
if goal in kb.facts:
    print(f"{goal} is proven!")
else:
    print(f"{goal} cannot be proven.")

# Display all inferred facts
print("Inferred Facts:")
for fact in kb.facts:
    print(fact)
