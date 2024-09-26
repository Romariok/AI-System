from pyswip import Prolog
from pyswip.prolog import PrologError

class PrologQuery:
    def __init__(self, path_to_base):
        self.prolog = Prolog()
        try:
            self.prolog.consult(path_to_base)
        except PrologError:
            print(f"Could not read knowledge base by path: {path_to_base}.")
            exit(22)

    def _query_and_extract(self, query, key):
        return [result[key] for result in self.prolog.query(query)]

    def get_available_roles(self):
        return self._query_and_extract("role(Role).", "Role")

    def get_available_attributes(self):
        return self._query_and_extract("attribute(Attribute).", "Attribute")

    def get_available_types(self):
        return self._query_and_extract("type(Type).", "Type")

    def get_difficulty(self, hero):
        query = f"hero_difficulty('{hero}', Difficulty)."
        result = list(self.prolog.query(query))
        return result[0]["Difficulty"] if result else None

    def look_for_matching_heroes(self, attributes, types, roles):
        query_parts = [
            "hero(Hero)",
            self._build_or_clause("hero_attribute(Hero, {})", attributes),
            self._build_or_clause("hero_role(Hero, {})", roles),
            self._build_or_clause("hero_type(Hero, {})", types)
        ]
        query = ', '.join(query_parts) + '.'
        
        matching_heroes = self._query_and_extract(query, "Hero")
        return [f"{hero}({self.get_difficulty(hero)})" for hero in matching_heroes]

    @staticmethod
    def _build_or_clause(template, items):
        if not items:
            return "(true)"
        clauses = [template.format(item) for item in items]
        return "(" + "; ".join(clauses) + ")"