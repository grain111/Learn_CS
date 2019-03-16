let current_channel;

document.addEventListener("DOMContentLoaded", () => {

  function add_channel(channel_name) {
    let option = document.createElement('option');
    option.innerHTML = channel_name;
    document.querySelector("#channel_list").appendChild(option);
  };

function add_message(data) {
  if (current_channel == data.channel) {
    message = document.createElement("li");
    message.innerHTML = data.message + " by " + data.user + " on " + data.timestamp;
    document.querySelector("#messages").appendChild(message);
  };
};

  socket.on("connect", () => {
    socket.emit("fetch_channels", channel_list => {
      console.log("Fetching channels");
      for (let channel of channel_list) {
        add_channel(channel);
      };
    });

    socket.emit("fetch_messages", current_channel, messages => {
      for (let message of messages) {
        add_message(message);
      };
    });
  });

  document.querySelector("#add_channel").onsubmit = data => {
    clear_error();
    socket.emit("add_channel", {"channel_name": data.srcElement.elements[0].value});
    document.querySelector("#channel_name").value = "";
    return false;
  };

  document.querySelector("#send_message").onsubmit = data => {
    let message = {message: data.srcElement.elements[0].value, channel: current_channel};
    console.log(message);
    socket.emit("send_message", {message: data.srcElement.elements[0].value, channel: current_channel});
    document.querySelector("#message_field").value = "";
    return false;
  };

  socket.on("new_channel", channel_name => {
    add_channel(channel_name);
  });

  socket.on("new_message", data => {
    add_message(data);
  });

  document.querySelector("#channel_list").onchange = () => {
    current_channel = document.querySelector("#channel_list").selectedOptions[0].value;
    socket.emit("fetch_messages", current_channel, messages => {
      document.querySelector("#messages").innerHTML = "";
      for (let message of messages) {
        add_message(message);
      };
    });

  };
});
