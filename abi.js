        var message = "I Love You";
        var index = 0;
        function typeMessage() {
          if (index < message.length) {
            document.getElementById("message").innerHTML += message.charAt(index);
            index++;
            setTimeout(typeMessage, 202);
          } 
          else {
            index = 0;
            document.getElementById("message").innerHTML = "";
            setTimeout(typeMessage, 520);
          }
        }
        typeMessage();
