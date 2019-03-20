socket.on("error", error_message => {
  document.querySelector("#error_handle").innerHTML = error_message;
});

function clear_error() {
  document.querySelector("#error_handle").innerHTML = "";
}
