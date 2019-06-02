document.addEventListener("DOMContentLoaded", _ => {
  let form = document.querySelector("#order_form")
  form.onsubmit = data => {
    let order = window.localStorage.getItem("order")
    let order_field = document.createElement("input")
    order_field.name = "order"
    order_field.value = order
    order_field.hidden = true
    form.appendChild(order_field)
    form.submit()
    return false
  }
})
