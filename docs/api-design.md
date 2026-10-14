# API Design: Tickets Service

## API Endpoints Table

| Purpose | Method | Route | Success Code | Error Codes |
| :--- | :--- | :--- | :--- | :--- |
| Create ticket | POST | `/tickets` | 201 | 422 invalid body, 401 not logged in |
| List tickets (with filters) | GET | `/tickets` | 200 | 401 not logged in, 400 invalid filter |
| Get one ticket | GET | `/tickets/{id}` | 200 | 401 not logged in, 404 not found |
| Update a ticket’s status | PATCH | `/tickets/{id}` | 200 | 401 not logged in, 403 forbidden, 404 not found, 422 invalid status |
| Delete a ticket | DELETE | `/tickets/{id}` | 204 | 401 not logged in, 403 forbidden, 404 not found |

---

## Design Decisions

1. **For a status change, would you use PUT or PATCH?**
   We use PATCH because we are modifying only a single field (the status) rather than replacing the entire ticket resource.

2. **What should “get one ticket” return when the ticket doesn’t exist?**
   It should return a `404 Not Found` status code because the targeted resource does not exist in the system.

3. **If someone deletes a ticket twice, what should the second call return? Is DELETE idempotent in your design?**
   The second call should return `404 Not Found` (or `204 No Content`), and yes, DELETE is idempotent because the server state remains identically deleted after both calls.