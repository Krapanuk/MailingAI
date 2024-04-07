function checkEmailsAndCallPhp() {
  var threads = GmailApp.getInboxThreads(0, 5); // Get first 5 threads from inbox
  for (var i = 0; i < threads.length; i++) {
    var messages = threads[i].getMessages();
    for (var j = 0; j < messages.length; j++) {
      var message = messages[j];
      var sender = message.getFrom();
      if (sender.includes("SenderToBeProcessed@anymail.net")) { // The Google Apps Script only processes mails from this sender
        if (message.isUnread()) {   // Only process unread messages to not process a mail twice
          var subject = message.getSubject();
          var body = message.getPlainBody();
          var emailFrom = sender;
          var url = 'https://www.....com/mailResponseServer.php'; // Path to php-script on your webserver
          var payload = {
            'subject': subject,
            'body': body,
            'sender': emailFrom
          };
          var options = {
            'method': 'post',
            'contentType': 'application/x-www-form-urlencoded',
            'payload': payload
          };
          
          UrlFetchApp.fetch(url, options);
          message.markRead();  // Mark processed message as read to not process it twice
        }
      }
    }
  }
}
