# Tool-routed agent with following tools
## Common notes:
- Our current agent working with smallest LLM is intendent only for tool calls (no for common questions). So far let leave it as is. We cannot get from smallest model more<br>
- The structure of JSON is {<br>
  "tool": "< tool_name >",<br>
  "arguments": { <br>
    "< arg_name >": "< value >"<br>
  }<br>
}<br>
- all methods of tools take dict as parameters. No need to update it.<br>
- You need to update signature of existing get_current_weather tool method <br>
- If no required parameter is provided return appropriate response like "to_currency is not provided"<br>
- consider  match: re.Match = re.search(regex, text, re.DOTALL) re.DOTALL means that "\n" (new line) will match metasymbols (*,., +) as well as any symbol. <br> With no re.DOTALL no match will work for the provided JSON's

## get_current_weather(arguments: dict)
access to a city as arguments.get("city")<br>
use "http://api.weatherapi.com/v1/current.json" with API_KEY that may be eceived from the cite free of cost
## get_exchange_rate(arguments: dict)
access to from_currency as arguments.get("from_currency") <br>
access to to_currency as arguments.get("to_currency") <br>
use https://data.fixer.io/api/latest with API_KEY that may be eceived from the cite free of cost<br>
bonus: think of caching (Take into consideration that data are updated once a day, but it should be configured)

