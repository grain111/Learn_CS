document.addEventListener("DOMContentLoaded", () => {

  function add_channel(channel_name) {
    let option = document.createElement('option');
    option.innerHTML = channel_name;
    document.querySelector("#channel_list").appendChild(option);
  };

  socket.on("connect", () => {
    socket.emit("fetch_channels", channel_list => {
      console.log("Fetching channels");
      for (let channel of channel_list) {
        add_channel(channel);
      };
    });
  });

  document.querySelector("#add_channel").onsubmit = data => {
    clear_error();
    socket.emit("add_channel", {"channel_name": data.srcElement.elements[0].value});
    document.querySelector("#channel_name").value = "";
    return false;
  };

  socket.on("new_channel", channel_name => {
    add_channel(channel_name);
  });

  document.querySelector("#channel_list").onchange = () => {
    let channel = document.querySelector("#channel_list").selectedOptions[0].value;
    socket.emit("fetch_messages", channel, messages => {
      console.log(messages);
    });

  };
});
