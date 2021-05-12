import requests


class Register:
    post_url = 'https://uda.or.ke/signup/'

    def post(self, data, skip = False):
        default = {
            'success' : False,
            'details': data
        }


        # skip records with member number
        if skip and data['member_no']:
            return default


        # send post request
        req = requests.post(self.post_url, data = {
            'csrf-token:': '',
            'referral': '0',
            'id_number': data['id_no'],
            'names': data['name'],
            'phone': data['contact'],
            'email': '',
            'county': '47',
            'constituency': '277',
            'ward': '1384',
            'membership': 'membership'
        })

        # print message
        res_json = req.json()
        if res_json:
            print(
                data['index'] + ':',
                data['id_no'] + ':',
                data['name'] + ':', 
                res_json['message']
            )

        # retun success
        if res_json['status'] == 'success':
            # get member number
            string_search = 'UDA member No. '
            index = res_json['message'].rindex(string_search) + len(string_search)
            data['member_no'] = res_json['message'][index:]

            return {
                'success' : True,
                'data': res_json,
                'details': data
            }


        # return default
        return default