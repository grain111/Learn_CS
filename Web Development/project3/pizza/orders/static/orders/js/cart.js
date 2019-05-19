function get_previous_sibling(element, selector) {
  let sibling = element.previousElementSibling;
  while (sibling) {
    if (sibling.matches(selector)) return sibling;
    sibling = sibling.previousElementSibling;
  };
};

function update_cart() {
  let cart = document.getElementById("cart");
  let items;
  if (document.querySelectorAll("#cart ul").length == 0){
    items = document.createElement("ul");
    cart.appendChild(items);
  } else {
    items = document.querySelector("#cart ul");
  };
  items.innerHTML = "";
  for (item of JSON.parse(window.localStorage.getItem("order")).items){
    let li = document.createElement("li");
    li.innerHTML = `${item.size} ${item.group} ${item.name}`;
    if (item.extras.length > 0){
      li.innerHTML += ` with ${item.extras}`;
    };

    items.appendChild(li);
  };
};



document.addEventListener('DOMContentLoaded', () => {
  let order = {};
  if (window.localStorage.getItem("order")){
    order = JSON.parse(window.localStorage.getItem("order"));
    update_cart();
  } else {
    order = {"items":[],
             "total": 0};
  };

  document.querySelectorAll(".menu_item__button").forEach(button =>{
    button.onclick = () => {
      // Getting extra choices
      let choices = [];
      let choices_value = 0;
      let extras = get_previous_sibling(button, ".menu_item__extra_choices").childNodes;
      for (extra of extras) {
        if (extra.tagName == "SELECT") {
          if (extra.options[extra.selectedIndex].value != "None"){
            choices_value += parseFloat(extra.options[extra.selectedIndex].dataset.price);
            choices.push(extra.options[extra.selectedIndex].value);
          };
        };
      };

      // Getting size
      size_choice = get_previous_sibling(button, ".menu_item__price").childNodes;
      let size = "small";
      let value = 0;
      for (child of size_choice){
        if (child.tagName == "SELECT"){
          value = parseFloat(child.options[child.selectedIndex].dataset.price);
          size = child.options[child.selectedIndex].value;
        } else if (child.tagName == "P"){
          value = parseFloat(child.dataset.price);
        };
      };

      // Getting item name
      let name = get_previous_sibling(button, ".menu_item__title").innerHTML;

      // Getting Group
      let group = get_previous_sibling(button.parentElement, ".menu_group__title").innerHTML;

      // Creating order item object and save object in session
      let order_item = {group: group,
                        name: name,
                        extras: choices,
                        size: size,
                        price: choices_value + value}
      order.items.push(order_item);
      order.total += order_item.price;

      window.localStorage.setItem("order", JSON.stringify(order));
      update_cart();
    };
  });
});
