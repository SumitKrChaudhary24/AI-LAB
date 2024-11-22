def unify(x, y, substitutions=None):
    """
    Perform unification of two terms in First-Order Logic.

    Parameters:
    - x: First term (can be a variable, constant, or compound expression).
    - y: Second term (same types as x).
    - substitutions: Dictionary of current substitutions.

    Returns:
    - Dictionary of substitutions if unification succeeds.
    - "FAILURE" if unification fails.
    """
    if substitutions is None:
        substitutions = {}

    # Step 1: Apply existing substitutions to x and y
    x = apply_substitutions(x, substitutions)
    y = apply_substitutions(y, substitutions)

    # Step 2: Handle identical terms
    if x == y:
        return substitutions

    # Step 3: Handle variables
    if is_variable(x):
        return unify_variable(x, y, substitutions)
    if is_variable(y):
        return unify_variable(y, x, substitutions)

    # Step 4: Handle compound expressions (predicates or functions)
    if is_compound(x) and is_compound(y):
        if predicate_symbol(x) != predicate_symbol(y):
            return "FAILURE"
        if len(arguments(x)) != len(arguments(y)):
            return "FAILURE"
        for arg_x, arg_y in zip(arguments(x), arguments(y)):
            substitutions = unify(arg_x, arg_y, substitutions)
            if substitutions == "FAILURE":
                return "FAILURE"
        return substitutions

    # Step 5: If terms are incompatible
    return "FAILURE"


def is_variable(term):
    """Check if a term is a variable (lowercase strings represent variables)."""
    return isinstance(term, str) and term.islower()


def is_compound(term):
    """Check if a term is a compound expression (e.g., predicates or functions)."""
    return isinstance(term, tuple) and len(term) > 1


def predicate_symbol(term):
    """Extract the predicate symbol or function name from a compound expression."""
    return term[0]


def arguments(term):
    """Extract the arguments of a compound expression."""
    return term[1:]


def unify_variable(var, value, substitutions):
    """Unify a variable with a value while checking for circular substitutions."""
    if var in substitutions:
        return unify(substitutions[var], value, substitutions)
    if value in substitutions:
        return unify(var, substitutions[value], substitutions)
    if occurs_check(var, value, substitutions):
        return "FAILURE"
    substitutions[var] = value
    return substitutions


def occurs_check(var, value, substitutions):
    """Ensure a variable does not appear within its own substitution."""
    if var == value:
        return True
    if is_compound(value):
        return any(occurs_check(var, arg, substitutions) for arg in arguments(value))
    return False


def apply_substitutions(term, substitutions):
    """Apply current substitutions to a term."""
    if is_variable(term) and term in substitutions:
        return apply_substitutions(substitutions[term], substitutions)
    if is_compound(term):
        return (predicate_symbol(term),) + tuple(
            apply_substitutions(arg, substitutions) for arg in arguments(term)
        )
    return term


# Example Usage
if __name__ == "__main__":
    term1 = ("Eats", "x", "Mango")  # Represents Eats(x, Apple)
    term2 = ("Eats", "Sumit", "y")  # Represents Eats(Riya, y)
    result = unify(term1, term2)
    print("Substitutions:", result)
