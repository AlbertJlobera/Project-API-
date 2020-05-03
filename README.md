# <h1 class="has-text-align-center"><strong>API Chat Project</strong></h1>

<h2>The perfect API to chat with other users, knowing the sentiment of the community</h2>


<p>We create a chat system to store users, differents chats topics and messages. Moreover, we use machine learning to analyse the sentiment of the message to detect the users behaivour.</p>

<p>To use the API we have differents parametres where you can request information about the chat. 
First of all, you will need to register a user name, then you will be able to enjoy the chats and write messages.</p>

<h3 class="has-text-align-center"><strong>Programs used to develop the API</strong></h3>

<p>We use the Framework Flask to create our API,we choose MongoDB as our database to store the data and we work with NLTK library for the sentimental analysis.</p>

<h3 class="has-text-align-center"><strong>Parametres</strong></h3>

<p><strong>First Parametre.</strong> To create an user name: 
 <i> [http://localhost:3500/create/user/<username>]</i></p>
 
 
<p><strong>Second Parametre.</strong> To assign user to a chat: 
 <i> [http://localhost:3500/chat/<chatname>/user/<username>]</i> </p>


<p><strong>Third Parametre.</strong> To add a new message to a specific chat:   <i>[http://localhost:3500/chat/<chatname>/user/<username>/message/<message>] </i> </p>
  
  
<p><strong>Fourth Parametre.</strong> Get all message from a chat as a list:
  <i>[http://localhost:3500/chat/<chatname>/list]</i> </p>
  
  
<p><strong>Fifth Parametre.</strong> Analyse the sentiment to a chat:
  <i> [http://localhost:3500/chat/<chatname>/sentiment]</i>  </p>
  
  
  
<h5 class="has-text-align-center"><strong>Let's chat!</strong></h5>
  
  
