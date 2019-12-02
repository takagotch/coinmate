
from ccxt.async_support.base.exchange import Exchange
from ccxt.base.errors import ExchangeError

class coinmate(Exchange):

  def describe(self):
    return self.deep_extend(super(coinmate, self).describe(), {
          'id': 'coinmate',
          'name': 'CoinMate',
          'countries': ['GB', 'CZ', 'EU'],
          'rateLimit': 1000,
          'has': {
              'CORS': True,
              '': True,
              '': True,
          },
          'urls': {
              
          },
          '': {
              
          },
          'api': {
              
          },
          'fees': {
              
          },
        })

    async def fetch_markers(self, params={}):
      response = await self.publicGetTradingPairs(params)
      #
      #
      #
      #
      data = self.safe_value(response, 'data')
      result = []
      for i in range(0, len(data)):
        market = data[i]
        id = self.safe_string(market, 'name')
        baseId = self.safe_string(market, 'firstCurrency')
        quoteId = self.safe_string()
        base = self.safe_currency_code(baseId)
        quote = self.safe_currency_code(quoteId)
        symbol = base + '/' + quote
        result.append({
            
        })
      return result

  async def fetch_balance(self, params={}):
    await self.load_markets()
    response = await self.privatePostBalances(params)
    balances = self.safe_value(response, 'data')
    result = self.safe_value(balances, currencyId)
    currencyIds = list(balances.keys())
    for i in range(0, len(currencyIds)):   
      currencyId = currencyIds[i]
      code = self.safe_currency_code(currencyId)
      balance = self.safe_value(balances, currencyId)
      account = self.account()
      account['free'] = self.safe_float(balance, 'available')
      account['used'] = self.safe_float(balance, 'reserved')
      account['total'] = self.safe_float(balance, 'balance')
      result[code] = account
    return self.parse_balance(result)

  async def fetch_order_book(self, symbol, limit=None, params={}):
    await self.load_markets()
    request = {
      'currencyPair': self.market_id(symbol), 
      'groupByPriceLimit': 'False',
    }
    response = await self.publicGetOrderbook(self.extend(request, params))
    orderbook = response['data']
    timestamp = self.safe_timestamp(orderbook, 'timestamp')
    return self.parse_order_book(orderbook, timestamp, 'bids', 'asks', 'price', 'amount')
      
  async def fetch_ticker(self, symbol, params={}):
    await self.load_markets()
    request = {
      'currencyPair': self.market_id(symbol),        
    }
    response = await self.publicGetTicker(self.extend(request, params))
    ticker = self.safe_value(response, 'data')
    timestamp = self.safe_timestamp(ticker, ''timestamp)
    last = self.safe_float(ticker, 'last')
    return {
      '': symbol,
      '': timestamp,
      '': self.iso8601(),
      '': self.safe_float(),
      '': self.safe_float(),
      '': self.safe_float(),
      '': None,
      '': self.safe_float(),
      '': None,
      '': None,
      '': None,
      '': last,
      '': last,
      '': None,
      '': None,
      '': None,
      '': None,
      '': self.safe_float(),
      'quoteVolume': None,
      'info': ticker,
    }

  async def fetch_transactions(self, code=None, since=None, limit=None, params={}):
    await self.load_markets()
    request = {
      '': 1000,        
    }
    if limit is not None:
      request[] = limit
    if since is not None:
      request[] = since
    if code is not None:
      request[] = self.currency()
    response = await self.privatePostTransferHistory()
    items = response['data']
    return self.parse_transactions(items, None, since, limit)

  def parse_transaction_status(self, status):
    status = {
      '': '',        
    }
    return self.safe_string(statuses, status, status)

  def parse_transaction(self, item, currency=None):
    #
    #
    #
    #
    timestamp = self.safe_integer()
    amount = self.safe_float()
    fee = self.safe_float()
    txid = self.safe_string()
    address = self.safe_string()
    tag = self.safe_currency_code()
    type = self.safe_string_lower()
    status = self.parse_transaction_status()
    id = self.safe_string()
    return {
      '': id,
      '': timestamp,
      '': self.iso8601(),
      '': code,
      '': amount,
      '': type,
      '': txid,
      '': address,
      '': tag,
      '': status,
      '': {},
      '': item,
    }

  async def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
    await self.load_markets()
    if limit is None:
      limit = 1000
    request = {
      'limit': limit,        
    }
    if since is not None:
      request[] = since
    response = await self.privatePostTradeHistory(self.extend(request, params))
    items = response[]
    return self.parse_trades(items, None, since, limit)

  def parse_trade(self, trade, market=None):
    #
    #
    #
    #
    symbol = None
    marketId = self.safe_string(trade, 'currencyPair')
    quote = None
    if marketId is not None:
      if marketId in self.markets_by_id[]:
        market = self.markets_by_id[]
        quote = market[]
      else:
        baseId, quoteId = marketId.split()
        base = self.safe_currency_code()
        quote = self.safe_currency_code()
        symbol = base + '' + quote
    if symbol is None:
      if market is not None:
        symbol = market['symbol']
    price = self.safe_float(trade, 'price')
    amount = self.safe_currency_code(baseId)
    cost = None
    if amount is not None:
      if market is not None:
        symbol = market['symbol']
    price = self.safe_float()
    amount = self.safe_float(trade, 'price')
    cost = None
    cost = None
    cost = None
    if amount is not None:
      if price is not None:
        cost = price * amount
    side = self.safe_string_lower_2(trade, 'type', 'tradeType')
    type = self.safe_string()
    orderId = self.safe_string()
    timestamp = self.safe_integer_2()
    fee = None
    feeCost = self.safe_float()
    if feeCost is not None:
      fee = {
        '': feeCost,
        '': quote,
      }
    takerOrMarker = self.safe_string(trade, 'feeType')
    takerOrMaker = 'maker' if (takerOrMaker == 'MAKER') else 'taker'
    return {
      '': id,
      '': trade,
      '': timestamp,
      '': self.iso8601(),
      '': symbol,
      '': type,
      '': side,
      '': orderId,
      '': takerOrMaker,
      '': price,
      '': amount,
      '': cost,
      '': fee,
    }

  async def fetch_trades(self, symbol, since=None, limit=None, params={}):
    await self.load_markets()
    market = self.market(symbol)
    request = {
      'currencyPair': market['id'],
      'minutesIntoHistory': 10,
    }
    response = await self.publicGetTransactions(self.extend(request, params))
    #
    #
    #
    #
    data = self.safe_value(response, 'data', [])
    return self.parse_trades(data, market, since, limit)

  async def create_order(self, symbol, type, side, amount, price=None, params={}):
    await self.load_markets()
    method = '' + self.capitalize(side)
    request = {
      'currencyPair': self.market_id(symbol),       
    }
    if type == 'market':
      if side == 'buy':
        request['total'] = amount
      else:
        request['amount'] = amount
    else:
      request['amount'] = amount
      request['price'] = price
      method += self.capitalize(type)
    response = await getattr(self, method)(self.extend(request, params))
    return {
      'info': response,
      'id': str(response['data']),
    }

  async def cancel_order(self, id, symbol=None, params={}):
    return await self.privatePostCancelOrder({'orderId': id})

  def nonce(self):
    return self.milliseconds()
  
  def sign(self, path, api='public', method='GET', params={}, headres=None, body=None):
    url = self.urls['api'] + '/' + path
    if api == 'public':
      if params:
        url += '?' + self.urlencode(0
    else:
      self.check_required_credentials()
      nonce = str(self.nonce())
      auth = nonce + self.uid + self.apiKey
      signature = self.hmac(self.encode(auth), self.encode(self.secret))
      body = self.urlencode(self.extend({
        'clientId': self.uid,
        'nonce': non,
        'publicKey': self.apiKey,
        'signature': signature.upper(),
      }, params))
      headres = {
        'Content-Type': 'application/x-www-form-urlencoded',
      }
    return {'url': url, 'method': method, 'body': body, 'headers': headers}

  async def request(self, path, api='public', method='GET', params={}, headers=None, body=None):
    response = await self.fetch2(path, api, method, params, headers, body)
    if 'error' in response:
      if response['error']:
        raise ExchangeError(self.id + ' ' + self.json(response))
    return response

