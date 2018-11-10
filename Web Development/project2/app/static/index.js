document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#add_user').onclick = () => {

    // Setting up a request to server
    const request = new XMLHttpRequest();
    const name = document.querySelector("#user_name").value;
    request.open('POST', '/add_user');

    request.onload = () => {
      const payload = JSON.parse(request.responseText);
      if (payload.result === 'success') {
        const req = new XMLHttpRequest();
        req.open('GET', '/');
        req.send();

        req.onload = () => {
          var parser = new DOMParser()
          var el = parser.parseFromString(req.responseText, "text/xml");
          document.querySelector("body").innerHTML = el.querySelector("body").innerHTML;
        }
      }
    }

    // Adding data to request
    const payload = new FormData();
    payload.append('user_name', name);

    //Making a request
    request.send(payload);

    return false;
  };
});
