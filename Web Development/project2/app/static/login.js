document.addEventListener('DOMContentLoaded', () => {

  function clear_error() {
    document.querySelector("#error_handle").innerHTML = "";
  }

  document.querySelector('#add_user').onclick = () => {
    const username = document.querySelector("#user_name").value;
    socket.emit('login', {name: username});
    };

  socket.on("login_success", chat_content => {
    clear_error();
    document.querySelector("#main").innerHTML = chat_content;
  });

  socket.on("error", error_message => {
    document.querySelector("#error_handle").innerHTML = error_message;
  });
});
