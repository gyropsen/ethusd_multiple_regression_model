# ETHUSD multiple regression model

Определение собственных движений цены ETHUSD, исключив из них движения вызванные влиянием цены BTCUSDT. 
<br/>

Методику выбрал - множественная регрессионная модель
<br/>

<h4>Параметры для регрессионной модели:</h4>
- BZUSD - котировки цен на нефть марки BRENT.
- GOLD - котировки цен на золото.
- SPY - котировки цен на инвестиционный фонд, портфель которого состоит из акций компаний, учитывающихся при расчете 
индекса S&P500. <br/>
- NGUSD - котировки цен на натуральный газ. <br/>
- USDTUSD - котировки цен на токен Ethereum, который привязан к стоимости доллара США. <br/>
- USDX - котировки цен на Индекс доллара США (USDX или DXY) — показатель стоимости доллара США в сравнении с другими 
валютами. <br/>
- DJIA - котировки цен на Промышленный индекс Доу Джонса. <br/>
- LTCUSD - котировки цен на Лайткоин Доллар США. <br/>
- BNBUSD - это собственный токен Binance Smart Chain и Binance Chain, работающий на платформе Ethereum. <br/>
- XRPUSD - котировки цен на  XRP — внутренняя цифровая монета RippleNet — платформы, разработанной на базе данных 
распределенного реестра XRP Ledger. <br/>

<h4>Описание идеи</h4>
Т.к. рынок по определению изменчив, причем рынок криптовалют изменчив особенно, поэтому нужно быстро адаптироваться под
условия, чтобы модель была актуальной. Поэтому был выбран метод динамический. Т.е. динамический сбор данных, 
динамическое построение модели, её фильтрация, и, наконец, прогноз.

