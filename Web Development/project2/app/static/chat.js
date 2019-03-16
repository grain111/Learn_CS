document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#add_channel").onsubmit = data => {
    clear_error();
    socket.emit("add_channel", {"channel_name": data.srcElement.elements[0].value});
      document.querySelector("#channel_name").value = "";
    return false;
  };
});
