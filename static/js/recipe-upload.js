// RECIPE UPLOAD | ADD INGREDIENT FUNCTION
function addIngredient() {
    message = ""
    let ingredient = document.getElementById("recipe-ingredients-name").value;
    console.log(ingredient == '')
    if(ingredient == ''){
    message+="Must include ingredient name\n"
    }
    let amount = document.getElementById("recipe-ingredients-amount").value;

    if(amount == "" || isNaN(amount)){
    message+="Must include a number as ingredient amount\n"
    }
    let unit = document.getElementById("recipe-ingredients-unit").value;
    console.log(unit)
    if(unit == "default"){
    message+="Must include ingredient unit\n"
    }
    let result = ingredient + amount + unit;
    console.log(result)
    if(message == ""){

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
    }
    else{
        form_alert(message)
    }
};


function submit_recipe(user_id) {
message = ""
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
    if(ingredient_list.length==0){ message+="Must add ingredients\n" }

    title = $("#recipe-title").val()
    if (title == ""){ message += "Must include a recipe title\n" }

    serves= $("#recipe-serves").val()
    if(serves == ""){ serves = 0}
    else if(isNaN(serves)){ message += "Servings must be a number" }

    cook_time= $("#recipe-cook-time").val()
    if(cook_time == ""){cook_time = "?? hours"}

    calories= $("#recipe-calories").val()
    console.log(isNaN(calories))
    if(calories == ""){calories=0}
    else if(isNaN(calories)){message += "Calories must be a number"}

    directions= $("#recipe-directions").val()
    if (directions == ""){
        message += "Must include directions\n"
    }
    image_url = $('#image-upload').val()
    if(image_url==""){ image_url=null}
    else if(!check_url(image_url)){message+="Must include a valid url for recipe image"}
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
    'meal_type': meal_type,
    'photo_url': image_url,
    'user_id': user_id
    }
 recipe_data =  {
    recipe_params: recipe_params,
    ingredients: ingredient_list
  }
console.log(recipe_data)
console.log(names, amounts, units);
 if(message != ""){
    form_alert(message)
    }
 else{
    $.ajax({
    type:"POST",
    contentType: "application/json",
    url: post_url,
    dataType: "json",
    data: JSON.stringify(recipe_data),
    complete : function(result) {
        id=result.responseText
      console.log("New ID: "+id);
      redirect_to_recipe(id)
    }});
 }
//  $.post(post_url,
//  {
//    recipe_params: recipe_params,
//    ingredients: ingredient_list
//  },
//  function(data, status){
//    alert("Data: " + data + "\nStatus: " + status);
//  });




}
//console.log(post_url)

function form_alert(message){
    console.log(message)
    alert(message)
}

function check_url(string){
let url;

  try {
    url = new URL(string);
  } catch (_) {
    return false;
  }

  return url.protocol === "http:" || url.protocol === "https:";
}