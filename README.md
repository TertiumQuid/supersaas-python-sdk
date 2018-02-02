# SuperSaaS Python SDK

Online bookings/appointments/calendars in Python using the SuperSaaS scheduling platform - https://supersaas.com

## Prerequisites

1. [Register for a (free) SuperSaaS account](https://www.supersaas.com/accounts/new), and
2. get your account name and password. 

##### Dependencies

Python 2.7 or 3.*

No external libraries. The supporting `urllib`/`urllib2` and `json`/`simplejson` standard libs are loaded conditionally.

## Configuration

Set the SuperSaaS `Client` authorization credentials (e.g. with keys/values from system environment):

    from SuperSaaS.SDK import Client
    Client.instance().configure(
        account_name=ENV['your-env-supersaas-account-name'],
        password = ENV['your-env-supersaas-account-password'],
        user_name = ENV['your-env-supersaas-user-name']
    )

## API Methods

Details of the data structures, parameters, and values can be found on the developer documentation site:

https://www.supersaas.com/info/dev

## Additional Information

+ [SuperSaaS Registration](https://www.supersaas.com/accounts/new)
+ [Product Documentation](https://www.supersaas.com/info/support)
+ [Developer Documentation](https://www.supersaas.com/info/dev)
+ [Ruby SDK](https://github.com/TertiumQuid/supersaas-ruby-sdk)
+ [PHP SDK](https://github.com/TertiumQuid/supersaas-php-sdk)

Contact: [support@supersaas.com](mailto:support@supersaas.com)