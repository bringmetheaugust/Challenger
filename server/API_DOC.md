# REST API doc
 
 * ##### 👱user CRUD
    - [new search](#new_search)

 * ###### 🗜search params

    - [brand list](#brands)
    <!-- - [set diary](#setdiary)
    - [update diary](#updatediary)
    - [delete diary](#deletediary) -->

 * ###### ⛔️reports

    - [error report](#error_report)

***

## 👱User

<a name="new_search"></a>

#### new search (POST /api/user/start)

 * req

        body: dict

 * res

        status

## 🗜Search params

<a name="brands"></a>

#### brand list (GET `api/params/brands`)

 * ##### res

        list

## ⛔️Reports

<a name="error_report"></a>

#### error reports (POST `api/report/error`)

 * ##### query params

        source: server type
