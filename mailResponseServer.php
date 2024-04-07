<?php
require_once 'credentials.php';

$emailSubject = $_POST['subject'] ?? 'empty subject';
$emailSubjectEncoded = mb_encode_mimeheader($emailSubject, 'UTF-8', 'B');
$emailBody = $_POST['body'] ?? 'empty mail text';
$senderEmail = $_POST['sender'] ?? 'empty sender';

$receiverEmail = 'SenderToBeProcssed@anymail.net';  // Mail adress the AIs response-mailtext should be sent to
// Description of you personally to create better fitting mail responses
$whoAmI = "You are a helpful assistant answering the mails in the role of a 40 year old software developer, married with a beautiful wife. You have 2 kids and live in Germany near Bielefeld."

function getChatGptResponse($text) {
    global $api_key;
    $curl = curl_init('https://api.openai.com/v1/chat/completions');
    
    $postData = json_encode([
        'model' => 'gpt-4-turbo-preview',
        'messages' => [
            ["role" => "system", "content" => $whoAmI],
            ["role" => "user", "content" => $text]
        ],
    ]);
    
    curl_setopt_array($curl, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $postData,
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $api_key,
        ],
    ]);
    
    $response = curl_exec($curl);
    curl_close($curl);
    $decodedResponse = json_decode($response, true);
    
    return $decodedResponse['choices'][0]['message']['content'] ?? 'Sorry, I could not process that.';
}

if ($senderEmail == 'SenderToBeProcssed@anymail.net') { // The php script only processes mails from this sender(s)
    
    $emailBody = getChatGptResponse($emailBody);

    $headers = 'From: ' . $senderEmail . "\r\n" .
    'Reply-To: ' . $senderEmail . "\r\n" .
    'Content-Type: text/plain; charset=UTF-8' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();

    mail($receiverEmail, $emailSubjectEncoded, $emailBody, $headers);
}
?>
