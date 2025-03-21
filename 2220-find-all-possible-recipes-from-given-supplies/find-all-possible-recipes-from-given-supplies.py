class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        needs = {r: set(i) for r, i in zip(recipes, ingredients)}

        updated = True
        while updated:
            updated = False
            for r in recipes:
                if r in supplies:
                    continue
                
                if needs[r].issubset(supplies):
                    supplies.add(r)
                    updated = True
        
        return [r for r in recipes if r in supplies]