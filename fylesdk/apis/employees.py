from .api_base import ApiBase

class Employees(ApiBase):
    """Class for Employees APIs."""

    POST_EMPLOYEES = '/api/tpa/v1/employees'
    GET_EMPLOYEES = '/api/tpa/v1/employees'
    GET_EMPLOYEE_BY_ID = '/api/tpa/v1/employees/{0}'
    GET_EMPLOYEE_ADMIN = '/api/tpa/v1/employees/my_profile'
    GET_EMPLOYEES_COUNT = '/api/tpa/v1/employees/count'

    def post(self, data):
        """Create or Update Employees in bulk.

        Parameters:
            data (list): List of dicts in Employees schema.
        
        Returns:
            List with IDs from the new Employees.
        """
        return self._post_request(data, Employees.POST_EMPLOYEES)

    def get_by_id(self, employee_id=None):
        '''Get a the details of the Employee by Id

        Parameters:
            employee_id (str): Unique ID to find an Employee. Employee Id is our internal Id, it starts with prefix ou always. (required)

        Returns:
            Dict in Employee schema.
        '''

        return self._get_request({}, Employees.GET_EMPLOYEE_BY_ID.format(employee_id))

    def get(self, updated_at=None, offset=None, limit=None):
        """Get a list of existing Employees matching the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)

        Returns:
            List with dicts in Employees schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit
        }, Employees.GET_EMPLOYEES)

    def get_my_profile(self):
        '''Get a the Employee details of the admin

        Parameters:
            None

        Returns:
            Dict in Employee schema.
        '''
        return self._get_request({}, Employees.GET_EMPLOYEE_ADMIN)

    def count(self, updated_at=None):
        """Get the count of existing Employees.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)

        Returns:
            Count of Employees.
        """
        return self._get_request({
            'updated_at': updated_at
        }, Employees.GET_EMPLOYEES_COUNT)