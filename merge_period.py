import sys

from lxml import etree

root = etree.parse(sys.argv[1])

for activity in list(root.iter("iati-activity")):
    for result in list(activity.iter("result")):
        actual_indicators = {}
        for num, indicator in enumerate(list(result.iter("indicator"))):
            title = num
            title_element = indicator.find("title")
            if title_element is not None:
                narrative_element = title_element.find("narrative")
                if narrative_element is not None:
                    title = narrative_element.text.strip()

            if title in actual_indicators:
                indicator_element = actual_indicators[title]
                for period_element in indicator.iter("period"):
                    indicator_element.append(period_element)
                indicator.getparent().remove(indicator) 
            else:
                actual_indicators[title] = indicator

print(etree.tostring(root, pretty_print=True).decode())
