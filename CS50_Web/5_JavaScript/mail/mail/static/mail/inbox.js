document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Submit handler
  document.querySelector('#compose-form').addEventListener('submit', send_mail)

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#details-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#details-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get mails form API and show them in mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails)
      emails.forEach(item => {
        const element = document.createElement('div');
        element.innerHTML = `
        <span>
          <strong>${item.sender}</strong> <span class="subject">${item.subject}</span> <span class='timeStamp'>${item.timestamp}</span>
        </span>
        `;
        // Change bg color if user read mail.
        element.className = item.read ? 'read' : 'unread';

        // When user click on an email user should be taken to a view of content of the email.
        element.addEventListener('click',function (){
          email_view(item.id)
        });
        document.querySelector("#emails-view").append(element);
      }); 
  });
}

function send_mail(event){
  event.preventDefault();
  // send email to API or to server
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent')  
  });
}

function email_view(id){
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Hide prevuse view and show details view
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#details-view').style.display = 'block';

      // ... add html to this view that show email details
      document.querySelector('#details-view').innerHTML = `
      <div>
        <p><strong>From:</strong> ${email.sender}</p>
        <p><strong>To:</strong> ${email.recipients}</p>
        <p><strong>Subject:</strong> ${email.subject}</p>
        <p><strong>Timestamp:</strong> ${email.timestamp}</p>
        <span>
          <button class="btn btn-sm btn-outline-primary" id="reply-button">Reply</button>
          <button class="btn btn-sm btn-outline-dark" id="archive-button">${email.archived ? "UnArchive" : "Archive"}</button>
        </span>
        <hr>
        <p>${email.body}</p>
      </div>
      `
      // Make email readed
      if(!email.read){
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
            read: true
          })
        })
      }

      // Archive email
      document.querySelector('#archive-button').addEventListener('click', function() {
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: !email.archived
          })
        })
      });

      // Reply email
      document.querySelector('#reply-button').addEventListener('click', function() {
        
        // Routing to compose email
        compose_email();

        // Set value to feilds
        document.querySelector('#compose-recipients').value = email.sender;
        let subject = email.subject;
        if (subject.split(' ',1)[0] != "Re:"){
          subject = "Re: " + email.subject;
        }
        document.querySelector('#compose-subject').value = subject;
        document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: ${email.body}`;

      })
    } 
  );
}

