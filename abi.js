        var message = "I love you";
        var index = 0;
        
        function typeMessage() {
          if (index < message.length) {
            document.getElementById("message").innerHTML += message.charAt(index);
            index++;
            setTimeout(typeMessage, 100);
          }
        }
        
        typeMessage();
