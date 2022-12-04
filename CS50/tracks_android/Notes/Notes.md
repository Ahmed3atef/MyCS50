[Notes](https://cs50.harvard.edu/x/2020/tracks/mobile/android/notes/#notes)
===========================================================================

[Distribution Code](https://cs50.harvard.edu/x/2020/tracks/mobile/android/notes/#distribution-code)
---------------------------------------------------------------------------------------------------

Download this project's [distribution code](https://cdn.cs50.net/2019/fall/tracks/android/notes/notes.zip).

To open the distribution code, extract the ZIP, open Android Studio, select "Import project", and select the folder you extracted from the ZIP.

[What To Do](https://cs50.harvard.edu/x/2020/tracks/mobile/android/notes/#what-to-do)
-------------------------------------------------------------------------------------

-   Deleting Notes

[Deleting Notes](https://cs50.harvard.edu/x/2020/tracks/mobile/android/notes/#deleting-notes)
---------------------------------------------------------------------------------------------

So far, our Notes app can add and edit notes. Let's add the ability for a user to delete a note when they no longer need it.

First, add a new method called `delete` to the `NoteDao` interface. You'll probably want this method to take an `id` of the note to delete, and use a `DELETE` query.

Next, add a button to your layout for deleting notes. Exactly what the UI looks like is up to you! (If you're feeling ambitious, you can try implementing a UI that allows a user to swipe on a note from the list to delete it, much like many email apps on Android.)

Finally, wire up that UI to a method that calls your new `delete` method on the `NoteDao`. Depending on your UI, you might find the `finish` method helpful---this method will dismiss the current activity and go back to the previous one.

To test your app, try creating a few notes and then deleting them, to make sure the right things get deleted!

[How to Submit](https://cs50.harvard.edu/x/2020/tracks/mobile/android/notes/#how-to-submit)
-------------------------------------------------------------------------------------------

To submit your code with `submit50`, you may either: (1) upload your code to CS50 IDE and run `submit50` from inside of your IDE, or (2) install `submit50` on your own computer by running `pip3 install submit50` (assuming you have [Python 3](https://www.python.org/downloads/) installed).

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 cs50/problems/2020/x/tracks/android/notes
```