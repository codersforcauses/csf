# Navigate the Admin Dashboard

The admin dashboard can be found at `www.westillneedanaddress.com/admin` and all staff accounts will be able to access it.

![Django Dashboard](../img/dashboard.png)

## Database Tables

All tables from that are stored into the database can be seen here.

`Groups` can be ignored, this is a default table that Django sets up and it is not in use for our application.

The `Events` table will most likely be used the most by `Community Spirit Foundation` staff. You can create public events that will be displayed to all viewers of the webapp.

The `Mileage` table keeps track of all distances travelled each day by all users. You can expect this table will have the most data stored.

`Teams` can be created by any user, and users can only join a team if they are given the special `join code` from the team admin or other members currently in that team. It is important to note that a user can only be part of `one team`.

`Sub Teams` are used when an admin user of a team wants to divide team members into groups. For example, Team `Community Spirit Foundation` may have subteams `Full-time Staff`, `Volunteers`, `Contract/Temp Staff`.

The `Users` table shows a list of all registrations to the app. Passwords are secure and hashed for security reasons.

## Dashboard Navigation

You can view all table data by clicking on the blue table names.
