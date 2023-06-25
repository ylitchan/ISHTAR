from pybloom_live import ScalableBloomFilter
import json
#
# sbfilter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
# with open('listMembers.json', 'r') as f:
#     list_members = json.load(f)
# for i in list_members:
#     sbfilter.add(i)
with open('sbfilterMember', 'rb') as f:

    # sbfilter.fromfile(f)
    sbfilter=ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH).fromfile(f)
print(sbfilter.add(1672164728880398337))