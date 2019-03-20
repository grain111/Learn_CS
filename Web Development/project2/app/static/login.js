function submit_user() {
  const username = document.querySelector("#user_name").value;
  socket.emit('login', {name: username});
  };

socket.on("login_success", chat_content => {
  clear_error();
  document.querySelector("#main").innerHTML = chat_content;
  get_channels();
});
