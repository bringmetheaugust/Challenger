<!-- ## RestAPI list

 * ##### auth
    - [authorization](#authorization)
    - [login](#login)
    - [registration](#registration)
    - [logout](#logout)

 * ###### diary

    - [get diary](#getdiary)
    - [set diary](#setdiary)
    - [update diary](#updatediary)
    - [delete diary](#deletediary)

***

<a name="authorization"></a>

#### authorization (GET `api/auth`)

###### req (only cookies)

###### res

    _id: Number
    nickname: String

***

<a name="login"></a>

#### login (POST `api/auth/login`)

###### req

    nickname: String
    password: String
    
###### res

    body: {
      _id: Number
      nickname: String
    }

    // or

    message: String

***

<a name="registration"></a>

#### registration (POST `api/auth/registration`)

###### req

    nickname: String
    password: String
    email: String
    
###### res

    body: {
      _id: Number
      nickname: String
    }

    // or

    message: String

***

<a name="logout"></a>

#### logout (GET `api/auth/logout`)

###### req (only cookies)

###### res (none)

***

<a name="getdiary"></a>

#### get diary (GET `api/diary`)

###### req(only cookies)

###### res

    body: Array<INote>

***

<a name="setdiary"></a>

#### set diary (POST `api/diary`)

###### req

    title: String
    data: String

###### res

    body: <INote>

***

<a name="updatediary"></a>

#### update diary (PATCH `api/diary`)

###### req
    <INote>

###### res (only status)

***

<a name="deletediary"></a>

#### delete diary (DELETE `api/diary`)

###### req

###### res

*** -->
