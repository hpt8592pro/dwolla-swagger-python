#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class UpdateCustomer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'email': 'str',
            'ip_address': 'str',
            'type': 'str',
            'status': 'str',
            'address1': 'str',
            'address2': 'str',
            'city': 'str',
            'state': 'str',
            'postal_code': 'str',
            'date_of_birth': 'str',
            'ssn': 'str',
            'phone': 'str'
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'ip_address': 'ipAddress',
            'type': 'type',
            'status': 'status',
            'address1': 'address1',
            'address2': 'address2',
            'city': 'city',
            'state': 'state',
            'postal_code': 'postalCode',
            'date_of_birth': 'dateOfBirth',
            'ssn': 'ssn',
            'phone': 'phone'
        }
        
        
        self.first_name = None  # str
        
        
        self.last_name = None  # str
        
        
        self.email = None  # str
        
        
        self.ip_address = None  # str
        
        
        self.type = None  # str
        
        
        self.status = None  # str
        
        
        self.address1 = None  # str
        
        
        self.address2 = None  # str
        
        
        self.city = None  # str
        
        
        self.state = None  # str
        
        
        self.postal_code = None  # str
        
        
        self.date_of_birth = None  # str
        
        
        self.ssn = None  # str
        
        
        self.phone = None  # str
        

    def __repr__(self):
        properties = []
        for p in self.__dict__:
            if p != 'swaggerTypes' and p != 'attributeMap':
                properties.append('{prop}={val!r}'.format(prop=p, val=self.__dict__[p]))

        return '<{name} {props}>'.format(name=__name__, props=' '.join(properties))


