## Software Design Principles
Object-Oriented Programming
- **DATA**:
- **BEHAVIOR**:

Other types of programming:
1. Procedural:
    - order of code matters
    -
2. Functional:
    - data and behavior are kept separate
    -






## Development with Swagger and OpenAPI
**Application Programming Interfaces (API)** enable two different services to interact and complement each other.


"Design First"
- when developer experience matters
- when deliverying mission critical APIs
- when ensuring good commmunication


"Code First"
- when delivery speed matters
- when developing internal APIs



### YAML
Yet Another Markup Language

- Used for configuration files
- More human-readable

### OpenAPI Specification (OAS) 3.0
One of the most popular standards for designing human-readable API contracts

1. **Info & OpenAPI**: high-level overview of the API. Includes description, license, version, author info, and etc.
2. **Servers**: presents where API's servers are located through URLs
```
servers:
- url: https://development.xyz-server.com/v1
  description: Development Server
- url: https://staging.xyz-server.com/v1
  description: Staging Server
```
3. **Paths**: presents API's endpoints and corresponding HTTP methods
```
paths:
  /pet/{petId}:
    get:
      summary: Find pet by ID
      description: Returns a single pet
      parameters:
      - name: petId
        in: path
        description: ID of pet to return
        required: true
        schema:
          type: integer
          format: int64
      responses:
        200:
          description: successful operation
        400:
          description: Invalid ID supplied
          content: {}
        404:
          description: Pet not found
          content: {}
```
4. **External Docs**: additional informatin
5. **Tags**: can help better categorize API operations into groups
6. **Components**: can hold a set of reusable objects that can be referenced in any path item
```
 /pets:
    get:
      summary: Get all pets
      responses:
        '200':
          description: A list of pets.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Pet'
components:
  schemas:
    Pet:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
```
