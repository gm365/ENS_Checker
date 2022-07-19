# ENS 域名注册状态检查

import requests

# function to use requests.post to make an API call to the subgraph url
def run_query(query):
    # endpoint where you are making the request
    request = requests.post('https://api.thegraph.com/subgraphs/name/ensdomains/ens'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(
            request.status_code, query))


def ens_checker(name='amazon'):
    # The Graph query - Query ENS name information
    query = """
    {
    domains(where: {name:"%s.eth"}) {
        id
        name
        labelName
        labelhash
    }
    }
    """%(name)
    result = run_query(query)
    if result['data']['domains']:
        print(f"😭 {name}.eth 已被注册 ")
    else:
        print(f'✅ {name}.eth 还可以注册')
    return


def main():

    names = ['amazon','google','vitalik5']

    for name in names:
        try:
            ens_checker(name)
        except:
            print(f'{name} 检查失败，稍后请重试')

if __name__ == "__main__":
    main()
