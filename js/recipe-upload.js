// RECIPE UPLOAD | ADD INGREDIENT FUNCTION
function addIngredient() {

    let ingredient = document.getElementById("recipe-ingredients-name").value;
    let amount = document.getElementById("recipe-ingredients-amount").value;
    let unit = document.getElementById("recipe-ingredients-unit").value;
    let result = ingredient + amount + unit;
    console.log(result)

    let ingredientList = document.getElementById("ingredient-list");
    let newItem = document.createElement("li");
    let ingredientName = document.createElement("span");
    ingredientName.textContent = ingredient;
    let ingredientAmount = document.createElement("span");
    ingredientAmount.textContent = amount;
    let ingredientUnit = document.createElement("span");
    ingredientUnit.textContent = unit;
    let removeButton = document.createElement("button");

    removeButton.textContent = "X";
    removeButton.className = "remove-item"
    removeButton.onclick = function () {
        this.parentElement.remove();
    }

    ingredientName.className = ("new-ingredient-name");
    ingredientAmount.className = ("new-ingredient-amount");
    ingredientUnit.className = ("new-ingredient-unit");

    newItem.append(ingredientName);
    newItem.append(ingredientAmount);
    newItem.append(ingredientUnit);
    newItem.append(removeButton);

    ingredientList.append(newItem);
};