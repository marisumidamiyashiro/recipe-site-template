// RECIPE CARD CREATION
window.onload = (event) => {
    function createCard() {

        // NEW CARD
        const newCard = document.createElement('div');

        // CARD IMAGE
        const newCardImage = document.createElement('div');
        const newImage = document.createElement('img');

        // CARD INFO
        const newCardInfo = document.createElement('div');

        // TITLE AND SUBHEAD
        const newCardTitle = document.createElement('div');
        const newHeader = document.createElement('h1');
        const newSubHead = document.createElement('span');

        // CARD DETAILS
        const newCardDetails = document.createElement('div');
        const newList = document.createElement('ul');
        const newListItem = document.createElement('li');

        // CARD BUTTON
        const newButton = document.createElement('div');
        const newLink = document.createElement('a');

        // CARD INFO
        let title = "Pizza";
        let subhead = "Lunch";

        let serves = "5";
        let time = "1 hour";
        let calories = "100";

        let spanServes = document.createElement('span');
        let spanTime = document.createElement('span');
        let spanCalories = document.createElement('span');

        // IMAGE HEIGHT AND WIDTH
        newImage.height = 250;
        newImage.width = 250;

        // CLASS NAMES
        newCard.className = ("recipe-card");
        newCardImage.className = ("recipe-card-image");
        newCardInfo.className = ("recipe-card-info");
        newCardTitle.className = ("recipe-card-title");
        newSubHead.className = ('recipe-category');
        newCardDetails.className = ('recipe-card-details');
        newListItem.className = ('recipe-card-list');
        newButton.className = ('recipe-card-button');
        title.className = ('recipe-title');
        newLink.className = ('button');
        newList.className = ('recipe-card-list');

        // TEXT
        newHeader.textContent = title;
        newSubHead.textContent = subhead;
        spanServes.textContent = serves;
        spanTime.textContent = time;
        newLink.textContent = "View Recipe";
        spanCalories.textContent = calories;

        let li_serves = document.createElement('li');
        let spanServesBefore = document.createElement('span');
        let spanServesFull = document.createElement('span');
        spanServesBefore.textContent = "serves"
        spanServesFull.textContent = `${serves} people`

        li_serves.append(spanServesBefore);
        li_serves.append(spanServesFull);

        let li_time = document.createElement('li');
        let spanTimeBefore = document.createElement('span');
        let spanTimeFull = document.createElement('span');
        spanTimeBefore.textContent = "Cook Time"
        spanTimeFull.textContent = `${time}`

        li_time.append(spanTimeBefore);
        li_time.append(spanTimeFull);

        let li_calories = document.createElement('li');
        let spanCaloriesBefore = document.createElement('span');
        let spanCaloriesFull = document.createElement('span');
        spanCaloriesBefore.textContent = "Calories"
        spanCaloriesFull.textContent = `${calories}`

        li_calories.append(spanCaloriesBefore);
        li_calories.append(spanCaloriesFull);

        // APPEND
        newCardImage.append(newImage);
        newCard.append(newCardImage);

        newCardInfo.append(newCardTitle);
        newCardTitle.append(newHeader);
        newCardTitle.append(newSubHead);
        newCard.append(newCardInfo);

        newListItem.append(li_serves);
        newListItem.append(li_time);
        newListItem.append(li_calories);
        newList.append(newListItem);
        newCardDetails.append(newList);
        newCardInfo.append(newCardDetails);

        newButton.append(newLink);
        newCardInfo.append(newButton);
        newCard.append(newCardInfo);

        container = document.getElementById("recipes-container");
        container.append(newCard);
        console.log(newCard)

    };

    createCard()
    createCard()
    createCard()
    createCard()
};
