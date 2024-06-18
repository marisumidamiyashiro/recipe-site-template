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
    ingredientUnit.id = $('#recipe-ingredients-unit').find('option:selected').data('id')
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


function submit_recipe() {
//    names = $(".new-ingredient-name")
//    amounts = $(".new-ingredient-amount")
//    units = $(".new-ingredient-unit")
    ingredient_list = []
    var names = $(".new-ingredient-name").map(function() {
    return this.innerHTML;
}).get();
    var amounts = $(".new-ingredient-amount").map(function() {
    return this.innerHTML;
}).get();
    var units = $(".new-ingredient-unit").map(function() {
    return this.id;
}).get();

    for (let i = 0; i < names.length; i++){
        new_ingredient = {
        'label': names[i],
        'unit': units[i],
        'amount': amounts[i]
        }
        ingredient_list.push(new_ingredient)
    }

    title = $("#recipe-title").val()
    serves= $("#recipe-serves").val()
    cook_time= $("#recipe-cook-time").val()
    calories= $("#recipe-calories").val()
    directions= $("#recipe-directions").val()
    meal_type= $("#recipe-category").val()
    console.log(title)
    console.log(serves)
    console.log(cook_time)
    console.log(calories)
    console.log(directions)
    console.log(meal_type)

    recipe_params = {
    'name': title,
    'cook_time': cook_time,
    'servings': serves,
    'calories': calories,
    'instructions': directions,
    'meal_type': meal_type
    }
 recipe_data =  {
    recipe_params: recipe_params,
    ingredients: ingredient_list
  }

console.log(names, amounts, units);
//  $.post(post_url,
//  {
//    recipe_params: recipe_params,
//    ingredients: ingredient_list
//  },
//  function(data, status){
//    alert("Data: " + data + "\nStatus: " + status);
//  });
    $.ajax({
    type:"POST",
    contentType: "application/json",
    url: post_url,
    dataType: "json",
    data: JSON.stringify(recipe_data),
    success : function(result) {
      alert(result);
    },error : function(result){
       console.log(result);
    }
    });


}
//console.log(post_url)