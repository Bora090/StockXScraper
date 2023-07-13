import requests
import csv

session = requests.session()

class stockx:
    def headers(includeGraphQl: bool = True) -> dict:
        headers = {
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "accept-language": "en-US",
            "content-type": "application/json",
            "x-stockx-device-id": "588830b3-eeb9-435b-86a9-4153e86e4de4",
            "x-stockx-session-id": "6debfd7e-064f-4388-9052-ebc64708ac88"
        }
        if includeGraphQl:
            headers["apollographql-client-name"] = "Iron"
            headers["apollographql-client-version"] = "22023.07.02.04"
            headers["app-platform"] = "Iron"
            headers["app-version"] = "2023.07.02.04"
        headers["cookie"] = "__cf_bm=G WOgjPZGw2hvn9Ap8cO1Fz_D5x9rPZOPB2QO4w6PFs-1689254673-0-AfIzpsa20f3hFleB1dJzqYWc5ycLf7F1utEL79iYZwPFtzoxqJYgCAnSjMqxu9eOlXU/IF95CGS/sNKUmmBxyXc=; stockx_device_id=588830b3-eeb9-435b-86a9-4153e86e4de4; stockx_session_id=6debfd7e-064f-4388-9052-ebc64708ac88; stockx_session=f904cbf4-901d-4cf4-80b2-049ece985fe9; stockx_selected_region=NL; pxcts=9c2be902-2180-11ee-98ff-58564a46766d;"
        return headers

    def allBrowseFilters(type: str = "navigation") -> dict:
        return session.get("https://stockx.com/api/allBrowseFilters", params={"type": type}, headers=stockx.headers(False)).json()

    def getProduct(id: str, skipFavorite: bool = True) -> requests.Response | None:
        try:
            return session.post("https://stockx.com/api/p/e", json={
                    "query": "query GetProduct($id: String!, $currencyCode: CurrencyCode, $countryCode: String!, $marketName: String, $skipFavorite: Boolean!) {\n  product(id: $id) {\n    id\n    listingType\n    deleted\n    ...ProductMerchandisingFragment\n    ...AffirmCalloutFragment\n    ...BreadcrumbsFragment\n    ...BreadcrumbSchemaFragment\n    ...HazmatWarningFragment\n    ...HeaderFragment\n    ...NFTHeaderFragment\n    ...LastSaleFragment\n    ...UrgencyBadgeFragment\n    ...MarketActivityFragment\n    ...MediaFragment\n    ...MyPositionFragment\n    ...ProductDetailsFragment\n    ...ProductMetaTagsFragment\n    ...ProductSchemaFragment\n    ...ScreenTrackerFragment\n    ...SizeSelectorWrapperFragment\n    ...StatsForNerdsFragment\n    ...ThreeSixtyImageFragment\n    ...TrackingFragment\n    ...UtilityGroupFragment\n    ...FavoriteProductFragment @skip(if: $skipFavorite)\n  }\n}\n\nfragment ProductMerchandisingFragment on Product {\n  id\n  merchandising {\n    title\n    subtitle\n    image {\n      alt\n      url\n    }\n    body\n    trackingEvent\n    link {\n      title\n      url\n      urlType\n    }\n  }\n}\n\nfragment AffirmCalloutFragment on Product {\n  productCategory\n  urlKey\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      lowestAsk\n    }\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        lowestAsk\n      }\n    }\n  }\n}\n\nfragment BreadcrumbsFragment on Product {\n  breadcrumbs {\n    name\n    url\n    level\n  }\n}\n\nfragment BreadcrumbSchemaFragment on Product {\n  breadcrumbs {\n    name\n    url\n  }\n}\n\nfragment HazmatWarningFragment on Product {\n  id\n  hazardousMaterial {\n    lithiumIonBucket\n  }\n}\n\nfragment HeaderFragment on Product {\n  primaryTitle\n  secondaryTitle\n  condition\n  productCategory\n  reciprocal {\n    id\n    urlKey\n    variants {\n      id\n      traits {\n        size\n      }\n    }\n  }\n}\n\nfragment NFTHeaderFragment on Product {\n  primaryTitle\n  secondaryTitle\n  productCategory\n  editionType\n}\n\nfragment LastSaleFragment on Product {\n  id\n  market(currencyCode: $currencyCode) {\n    statistics(market: $marketName) {\n      ...LastSaleMarketStatistics\n    }\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      statistics(market: $marketName) {\n        ...LastSaleMarketStatistics\n      }\n    }\n  }\n}\n\nfragment LastSaleMarketStatistics on MarketStatistics {\n  lastSale {\n    amount\n    changePercentage\n    changeValue\n    sameFees\n  }\n}\n\nfragment UrgencyBadgeFragment on Product {\n  id\n  productCategory\n  primaryCategory\n  sizeDescriptor\n  listingType\n  market(currencyCode: $currencyCode) {\n    ...LowInventoryBannerMarket\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      ...LowInventoryBannerMarket\n    }\n  }\n  traits {\n    name\n    value\n    visible\n  }\n}\n\nfragment LowInventoryBannerMarket on Market {\n  bidAskData(country: $countryCode, market: $marketName) {\n    numberOfAsks\n    lowestAsk\n  }\n  salesInformation {\n    lastSale\n    salesLast72Hours\n  }\n}\n\nfragment MarketActivityFragment on Product {\n  id\n  title\n  productCategory\n  primaryTitle\n  secondaryTitle\n  media {\n    smallImageUrl\n  }\n}\n\nfragment MediaFragment on Product {\n  id\n  productCategory\n  title\n  brand\n  urlKey\n  variants {\n    id\n    hidden\n    traits {\n      size\n    }\n  }\n  media {\n    gallery\n    all360Images\n    imageUrl\n  }\n}\n\nfragment MyPositionFragment on Product {\n  id\n  urlKey\n}\n\nfragment ProductDetailsFragment on Product {\n  id\n  title\n  productCategory\n  browseVerticals\n  description\n  gender\n  traits {\n    name\n    value\n    visible\n    format\n  }\n}\n\nfragment ProductMetaTagsFragment on Product {\n  id\n  urlKey\n  productCategory\n  brand\n  model\n  title\n  description\n  condition\n  styleId\n  breadcrumbs {\n    name\n    url\n  }\n  traits {\n    name\n    value\n  }\n  media {\n    thumbUrl\n    imageUrl\n  }\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      lowestAsk\n      numberOfAsks\n    }\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n    }\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        lowestAsk\n      }\n    }\n  }\n}\n\nfragment ProductSchemaFragment on Product {\n  id\n  urlKey\n  productCategory\n  brand\n  model\n  title\n  description\n  condition\n  styleId\n  traits {\n    name\n    value\n  }\n  media {\n    thumbUrl\n    imageUrl\n  }\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      lowestAsk\n      numberOfAsks\n    }\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n    }\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        lowestAsk\n      }\n    }\n    gtins {\n      type\n      identifier\n    }\n  }\n}\n\nfragment ScreenTrackerFragment on Product {\n  id\n  brand\n  productCategory\n  primaryCategory\n  title\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      highestBid\n      lowestAsk\n      numberOfAsks\n      numberOfBids\n    }\n    salesInformation {\n      lastSale\n    }\n  }\n  media {\n    imageUrl\n  }\n  traits {\n    name\n    value\n  }\n  variants {\n    id\n    traits {\n      size\n    }\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        highestBid\n        lowestAsk\n        numberOfAsks\n        numberOfBids\n      }\n      salesInformation {\n        lastSale\n      }\n    }\n  }\n  tags\n  reciprocal {\n    id\n    variants {\n      id\n    }\n  }\n}\n\nfragment SizeSelectorWrapperFragment on Product {\n  id\n  ...SizeSelectorFragment\n  ...SizeSelectorHeaderFragment\n  ...SizesFragment\n  ...SizesOptionsFragment\n  ...SizeChartFragment\n  ...SizeChartContentFragment\n  ...SizeConversionFragment\n  ...SizesAllButtonFragment\n}\n\nfragment SizeSelectorFragment on Product {\n  id\n  title\n  productCategory\n  browseVerticals\n  sizeDescriptor\n  availableSizeConversions {\n    name\n    type\n  }\n  defaultSizeConversion {\n    name\n    type\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n    }\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n      }\n    }\n  }\n}\n\nfragment SizeSelectorHeaderFragment on Product {\n  sizeDescriptor\n  productCategory\n  availableSizeConversions {\n    name\n    type\n  }\n}\n\nfragment SizesFragment on Product {\n  id\n  productCategory\n  listingType\n  title\n}\n\nfragment SizesOptionsFragment on Product {\n  id\n  listingType\n  variants {\n    id\n    hidden\n    group {\n      shortCode\n    }\n    traits {\n      size\n    }\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n      }\n    }\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        lowestAsk\n      }\n    }\n  }\n}\n\nfragment SizeChartFragment on Product {\n  availableSizeConversions {\n    name\n    type\n  }\n  defaultSizeConversion {\n    name\n    type\n  }\n}\n\nfragment SizeChartContentFragment on Product {\n  availableSizeConversions {\n    name\n    type\n  }\n  defaultSizeConversion {\n    name\n    type\n  }\n  variants {\n    id\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n      }\n    }\n  }\n}\n\nfragment SizeConversionFragment on Product {\n  productCategory\n  browseVerticals\n  sizeDescriptor\n  availableSizeConversions {\n    name\n    type\n  }\n  defaultSizeConversion {\n    name\n    type\n  }\n}\n\nfragment SizesAllButtonFragment on Product {\n  id\n  sizeAllDescriptor\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      lowestAsk\n    }\n  }\n}\n\nfragment StatsForNerdsFragment on Product {\n  id\n  title\n  productCategory\n  sizeDescriptor\n  urlKey\n}\n\nfragment ThreeSixtyImageFragment on Product {\n  id\n  title\n  variants {\n    id\n  }\n  productCategory\n  media {\n    all360Images\n  }\n}\n\nfragment TrackingFragment on Product {\n  id\n  productCategory\n  primaryCategory\n  brand\n  title\n  market(currencyCode: $currencyCode) {\n    bidAskData(country: $countryCode, market: $marketName) {\n      highestBid\n      lowestAsk\n    }\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      bidAskData(country: $countryCode, market: $marketName) {\n        highestBid\n        lowestAsk\n      }\n    }\n  }\n}\n\nfragment UtilityGroupFragment on Product {\n  id\n  ...FollowFragment\n  ...FollowContentFragment\n  ...FollowShareContentFragment\n  ...FollowSuccessFragment\n  ...PortfolioFragment\n  ...PortfolioContentFragment\n  ...ShareFragment\n}\n\nfragment FollowFragment on Product {\n  id\n  productCategory\n  title\n  variants {\n    id\n    traits {\n      size\n    }\n  }\n}\n\nfragment FollowContentFragment on Product {\n  title\n}\n\nfragment FollowShareContentFragment on Product {\n  id\n  title\n  sizeDescriptor\n  urlKey\n  variants {\n    id\n    traits {\n      size\n    }\n  }\n}\n\nfragment FollowSuccessFragment on Product {\n  id\n  title\n  productCategory\n  sizeDescriptor\n  media {\n    smallImageUrl\n  }\n  variants {\n    id\n    traits {\n      size\n    }\n  }\n}\n\nfragment PortfolioFragment on Product {\n  id\n  title\n  productCategory\n  variants {\n    id\n  }\n  traits {\n    name\n    value\n  }\n}\n\nfragment PortfolioContentFragment on Product {\n  id\n  productCategory\n  sizeDescriptor\n  variants {\n    id\n    traits {\n      size\n    }\n  }\n}\n\nfragment ShareFragment on Product {\n  id\n  productCategory\n  title\n  media {\n    imageUrl\n  }\n}\n\nfragment FavoriteProductFragment on Product {\n  favorite\n}",
                    "variables": {
                        "id": id,
                        "currencyCode": "EUR",
                        "countryCode": "NL",
                        "marketName": "NL",
                        "skipFavorite": skipFavorite,
                    },
                    "operationName": "GetProduct",
                },
                headers=stockx.headers(),
            )
        except:
            return None

    def browse(
        category: str,
        tag: str,
        tags: list = [],
        page: int = 1,
        limit: int = 40,
        autoReturnParse=True,
    ) -> requests.Response | dict | None:
        try:
            response = session.post("https://stockx.com/api/p/e", json={
                    "query": "query Browse($category: String, $filters: [BrowseFilterInput], $filtersVersion: Int, $query: String, $sort: BrowseSortInput, $page: BrowsePageInput, $currency: CurrencyCode, $country: String!, $market: String, $staticRanking: BrowseExperimentStaticRankingInput, $skipFollowed: Boolean!) {\n  browse(\n    category: $category\n    filters: $filters\n    filtersVersion: $filtersVersion\n    query: $query\n    sort: $sort\n    page: $page\n    experiments: {staticRanking: $staticRanking}\n  ) {\n    suggestions {\n      isCuratedPage\n      relatedPages {\n        title\n        url\n      }\n      locales\n    }\n    results {\n      edges {\n        objectId\n        node {\n          ... on Product {\n            ...BrowseProductDetailsFragment\n            ...FollowedFragment @skip(if: $skipFollowed)\n            ...ProductTraitsFragment\n            market(currencyCode: $currency) {\n              ...MarketFragment\n            }\n          }\n          ... on Variant {\n            id\n            followed @skip(if: $skipFollowed)\n            product {\n              ...BrowseProductDetailsFragment\n              traits(filterTypes: [RELEASE_DATE, RETAIL_PRICE]) {\n                name\n                value\n              }\n            }\n            market(currencyCode: $currency) {\n              ...MarketFragment\n            }\n            traits {\n              size\n            }\n          }\n        }\n      }\n      pageInfo {\n        limit\n        page\n        pageCount\n        queryId\n        queryIndex\n        total\n      }\n    }\n    query\n  }\n}\n\nfragment FollowedFragment on Product {\n  followed\n}\n\nfragment ProductTraitsFragment on Product {\n  productTraits: traits(filterTypes: [RELEASE_DATE, RETAIL_PRICE]) {\n    name\n    value\n  }\n}\n\nfragment MarketFragment on Market {\n  currencyCode\n  bidAskData(market: $market, country: $country) {\n    lowestAsk\n    highestBid\n    lastHighestBidTime\n    lastLowestAskTime\n  }\n  state(country: $country) {\n    numberOfCustodialAsks\n  }\n  salesInformation {\n    lastSale\n    lastSaleDate\n    salesThisPeriod\n    salesLastPeriod\n    changeValue\n    changePercentage\n    volatility\n    pricePremium\n  }\n  deadStock {\n    sold\n    averagePrice\n  }\n  statistics {\n    last90Days {\n      averagePrice\n    }\n  }\n}\n\nfragment BrowseProductDetailsFragment on Product {\n  id\n  name\n  urlKey\n  title\n  brand\n  description\n  model\n  condition\n  productCategory\n  listingType\n  media {\n    thumbUrl\n    smallImageUrl\n  }\n}",
                    "variables": {
                        "query": "",
                        "category": category,
                        "filters": [
                            {"id": "_tags", "selectedValues": [tag]},
                            {"id": "browseVerticals", "selectedValues": [category]},
                            {"id": "currency", "selectedValues": ["EUR"]},
                        ]
                        + tags,
                        "filtersVersion": 4,
                        "sort": {"id": "featured", "order": "DESC"},
                        "page": {"index": page, "limit": limit},
                        "currency": "EUR",
                        "country": "NL",
                        "marketName": None,
                        "staticRanking": {"enabled": False},
                        "skipFollowed": True,
                    },
                    "operationName": "Browse",
                },
                headers=stockx.headers(),
            )
            print(response)
            if autoReturnParse:
                try:
                    return stockx.parseBrowse(response.json())
                except:
                    return None
            return response

        except:
            return None

    # by default we leave the children without parents :( so sad
    def filterChildren(includeParents=False) -> list:
        """
        Just a list of all the children filters / categories
        """
        categories = []
        for filter in stockx.allBrowseFilters():
            if includeParents:
                categories.append(filter["url"])
            for child in filter["children"]:
                categories.append(child["url"])
        return categories

    def filterFamily() -> list:
        """
        Just a list with a dict: of all the "filters" / categories\n
        {
            parent: str(parentUrl),
            children: list(childrenUrl)
        }
        """
        categories = []
        for filter in stockx.allBrowseFilters():
            newCategory = {}
            newCategory["parent"] = filter["url"]
            newCategory["children"] = [child["url"] for child in filter["children"]]
            categories.append(newCategory)
        return categories

    def browseFilterFamily() -> list:
        categories = []
        allBrowseFilters = stockx.allBrowseFilters("browse")
        for filter in allBrowseFilters:
            newCategory = {}
            newCategory["parent"] = filter.replace(" ", "-")
            if allBrowseFilters[filter]["children"]:
                for child in allBrowseFilters[filter]["children"]:
                    if child["name"] == "Brands":
                        newCategory["children"] = [
                            x["algolia"].replace(" ", "-") for x in child["children"]
                        ]
            if newCategory.get("children"):
                categories.append(newCategory)
        return categories

    def parseBrowse(responseJson: dict) -> dict:
        assert type(responseJson) != requests.Response
        results = responseJson["data"]["browse"]["results"]
        return {
            "totalPages": results["pageInfo"]["total"],
            "items": [node["node"] for node in results["edges"]],
        }


def get(origin, *args):
    for arg in args:
        if origin.get(arg):
            origin = origin.get(arg)
        else:
            return None
    return origin


# # print(stockx.getProduct("apple-airpods-fmax-headphones-pink").json())
items = []
for category in stockx.browseFilterFamily():
    for child in category["children"]:
        browse = stockx.browse(category["parent"], child)
        print(browse)
        if browse and browse.get("items") is not []:
            totalPages = browse["totalPages"]
            try:
                for item in stockx.browse(category["parent"], child, limit=40 * totalPages)["items"]:
                    newItem = {}
                    newItem["id"] = item.get("id")
                    newItem["brand"] = item.get("brand")
                    newItem["name"] = item.get("name")
                    newItem["title"] = item.get("title")
                    newItem["childCategory"] = child
                    newItem["parentCategory"] = category["parent"]
                    newItem["href"] = f"https://stockx.com/{item.get('urlKey')}"
                    newItem["retailPrice"] = None
                    if item.get("productTraits"):
                        for trait in item.get("productTraits"):
                            if trait.get("name") == "Retail Price":
                                newItem["retailPrice"] = trait.get("value")
                    newItem["lowestAsk"] = get(item, "market", "bidAskData", "lowestAsk")
                    newItem["highestBid"] = get(item, "market", "bidAskData", "highestBid")
                    newItem["lastSale"] = get(item, "market", "salesInformation", "lastSale")
                    newItem["lastSaleDate"] = get(item, "market", "salesInformation", "lastSaleDate")
                    newItem["amountSold"] = get(item, "market", "deadStock", "sold")
                    newItem["averagePrice"] = get(item, "market", "deadStock", "averagePrice")
                    items.append(newItem)
            except:
                continue

file = open("export.csv", "w", encoding="utf-8")
writer = csv.writer(file, delimiter=";")
print(items)
writer.writerow(items[0].keys())
for item in items:
    writer.writerow(item.values())
file.close()
