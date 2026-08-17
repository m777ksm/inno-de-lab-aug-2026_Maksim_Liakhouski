**Отчет по проектированию базы данных**

**Part 1: Выбор Сценария **

Для данной работы выбран сценарий: Управление арендной недвижимостью (офисные и производственные помещения для юрлиц в нескольких локациях). Эта система будет управлять объектами недвижимости, арендаторами, договорами, оплатами и обслуживанием недвижимости. 

**Part 2: Проектирование Базы Данных и Документация **

**Идентификация Сущностей и Атрибутов: **

1. Объекты аренды (Rental property)

2. Арендаторы (Tenants)

3. Договоры аренды (LeaseAgreement)

4. Аренда (Lease)

5. Заявки на обслуживание (ServiceRequest)

6. Обслуживающий персонал (Staff)

7. Выполнения заявок на обслуживание (ServiceRequestStaff)


**Проектирование Таблиц: **

1 **Table Name: RentalProperty **

  - Description: Хранит информацию об объектах недвижимости сдаваемых в аренду.

  - Attributes: 

    - *PropertyID:* INTEGER, PK, NOT NULL, UNIQUE 

    - *Address:* VARCHAR (200), NOT NULL

    - *RoomNumber:* SMALLINT

    - *Area:* INTEGER, NOT NULL

  - Constraints:

    - PK\_RentalProperty: PRIMARY KEY (PropertyID) 

    - UQ\_FullAddress: UNIQUE (Address, RoomNumber) 


2 **Table Name: Tenants **

  - Description: Хранит информацию об арендаторах.

  - Attributes: 

    - *TenantID:* INTEGER, PK, NOT NULL, UNIQUE 

    - *CompanyName:* VARCHAR (200), NOT NULL

    - *CompanyDetails:* TEXT, NOT NULL, UNIQUE

    - *PhoneNumber:* VARCHAR (30)

    - *Email:* VARCHAR (255), UNIQUE

  - Constraints:

    - *PK\_ Tenants:* PRIMARY KEY (TenantID) 

    - *UQ\_CompanyDetails:* UNIQUE

    - *UQ\_Email:* UNIQUE


3 **Table Name: LeaseAgreement**

  - Description: Хранит информацию о договорах аренды.

  - Attributes: 

    - *AgreementID:* INTEGER, PK, NOT NULL, UNIQUE 

    - *TenantID:* INTEGER, FK (REFERENCES Tenants), NOT NULL

    - *LeaseAgreementNumber:* INTEGER, NOT NULL

    - *AgreementDate:* DATE, NOT NULL, DEFAULT CURRENT\_DATE

    - *ExpirationDate:* DATE, NOT NULL

  - Constraints:

    - *PK\_ LeaseAgreement:* PRIMARY KEY (AgreementID)

    - *FK\_LeaseAgreement\_Tenants:* FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID)

    - UQ\_NumberDate: UNIQUE (LeaseAgreementNumber, AgreementDate) 

    - *CHK\_Dates:* CHECK (ExpirationDate \> AgreementDate) 


4 **Table Name: Lease**

  - Description: Хранит информацию о том, какие помещения и по каким договорам сдавались в аренду и сдаются в данный момент.

  - Attributes: 

    - *LeaseID:* INTEGER, PK, NOT NULL, UNIQUE

    - *AgreementID:* INTEGER, FK (REFERENCES LeaseAgreement), NOT NULL

    - *PropertyID:* INTEGER, FK (REFERENCES RentalProperty), NOT NULL

    - *StartDate:* DATE, NOT NULL, DEFAULT CURRENT\_DATE

    - *EndDate:* DATE, NOT NULL

    - *IsActive:* BOOLEAN, NOT NULL, DEFAULT TRUE

  - Constraints:

    - *PK\_ Lease:* PRIMARY KEY (LeaseID)

    - *FK\_Lease\_LeaseAgreement:* FOREIGN KEY (*AgreementID*) REFERENCES *LeaseAgreement*(*AgreementID*)

    - *FK\_Lease\_RentalProperty:* FOREIGN KEY (PropertyID) REFERENCES RentalProperty(PropertyID)

    - *UQ\_Lease:* UNIQUE (AgreementID, PropertyID, StartDate)

    - *CHK\_Dates:* CHECK (EndDate \> StartDate) 


5 **Table Name: ServiceRequest**

  - Description: Хранит информацию о запросах на обслуживание.

  - Attributes: 

    - *RequestID:* INTEGER, PK, NOT NULL, UNIQUE 

    - *TenantID:* INTEGER, FK (REFERENCES Tenants), NOT NULL

    - *PropertyID:* INTEGER, FK (REFERENCES RentalProperty), NOT NULL

    - *Desсription:* TEXT, NOT NULL

    - *Date:* DATE, NOT NULL, DEFAULT CURRENT\_DATE

    - *Completed:* BOOLEAN, NOT NULL, DEFAULT FALSE

  - Constraints:

    - *PK\_ ServiceRequest:* PRIMARY KEY (RequestID)

    - *FK\_ServiceRequest\_Tenants:* FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID)

    - *FK\_ServiceRequest\_RentalProperty:* FOREIGN KEY (PropertyID) REFERENCES RentalProperty(PropertyID)


6 **Table Name: Staff**

  - Description: Хранит информацию о персонале, выполняющем обслуживание.

  - Attributes: 

    - *StaffID:* INTEGER, PK, NOT NULL, UNIQUE 

    - *Profession:* VARCHAR (200), NOT NULL* *

    - *FirstName:* VARCHAR (100), NOT NULL* *

    - *LastName:* VARCHAR (100), NOT NULL

    - *MobileNumber:* VARCHAR (30), NOT NULL,UNIQUE

  - Constraints:

    - *PK\_ Staff:* PRIMARY KEY (StaffID)

    - *UQ\_MobileNumber:* UNIQUE


7 **Table Name: ServiceRequestStaff**

  - Description: Хранит информацию о номерах заявок на обслуживание и персонале, который их выполнял.

  - Attributes: 

    - *RequestID:* INTEGER, FK (REFERENCES ServiceRequest), NOT NULL

    - *StaffID:* INTEGER, FK (REFERENCES Staff), NOT NULL

  - Constraints:

    - *PK\_ ServiceRequestStaff:* PRIMARY KEY (RequestID, StaffID)

    - *FK\_ServiceRequestStaff\_ServiceRequest:* FOREIGN KEY (RequestID) REFERENCES *ServiceRequest*(RequestID)

    - *FK\_ServiceRequestStaff\_Staff:* FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)


Взаимосвязи:

- **Tenants и LeaseAgreement (Один-ко-Многим)**: Один Арендатор может заключить несколько договоров аренды недвижимости, но каждый договор аренды только с одним Арендатором. LeaseAgreement.TenantID является внешним ключом, ссылающимся на Tenants.TenantID

- **Rental Property и LeaseAgreement через промежуточную таблицу Lease (Многие-ко-Многим)**: С течением времени по одному объекту недвижимости может быть много заключено много договоров аренды и в каждом договоре аренды может указываться несколько объектов. Lease.PropertyID является внешним ключом, ссылающимся на RentalPropety.PropertyID. Lease.AgreementID является внешним ключом, ссылающимся на LeaseAgreement.AgreementID

- **Tenants и ServiceRequest (Один-ко-Многим)**: Один Арендатор может сделать много запросов в службу сервиса, но каждая запись относится только к одному Арендатору. ServiceRequest.TenantID является внешним ключом, ссылающимся на Tenants.TenantID

- **RentalProperty и ServiceRequest (Один-ко-Многим)**: На один объект недвижимости может быть сделано много запросов в службу сервиса, но каждый запрос относится только к одному объекту. ServiceRequest.PropertyID является внешним ключом, ссылающимся на RentalPropety.PropertyID

- **Staff и ServiceRequest через промежуточную таблицу ServiceRequestStaff (Многие-ко-Многим)**: На одну заявку на обслуживание отправляются разные специалисты и каждый специалист получает много заявок. ServiceRequestStaff.StaffID является внешним ключом, ссылающимся на Staff. StaffID. ServiceRequestStaff.RequestID является внешним ключом, ссылающимся на ServiceRequest.RequestID.

