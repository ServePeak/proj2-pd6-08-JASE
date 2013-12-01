
import stuyteachers


def num(a):
    return '{:,.0f}'.format(a)

def table_overpaid(limit):
    r = '<table class="table table-bordered"><tr class="danger"><th colspan="4" style="text-align:center;">Top '+str(limit)+' Overpaid Teachers</td></tr><tr class="danger"><th>&nbsp;</th><th>Teacher Name</th><th>Salary</th><th>Overall Rating</th></tr>'

    count = 0
    for x in stuyteachers.get_overpaid(limit):
        x['salary'] = num(x['salary'])
        count += 1
        r += '<tr class="danger"><td>'+str(count)+'</td><td><a href="teacher-%(id)d">%(first)s %(last)s</a><br /><small>%(title)s</small></td><td>$%(salary)s</td><td style="text-align:center">%(rmt_overall)d&#37;</td></tr>'%(x)

    r += '</table>'

    return r

def table_underpaid(limit):
    r = '<table class="table table-bordered"><tr class="success"><th colspan="4" style="text-align:center;">Top '+str(limit)+' Underpaid Teachers</td></tr><tr class="success"><th>&nbsp;</th><th>Teacher Name</th><th>Salary</th><th>Overall Rating</th></tr>'

    count = 0
    for x in stuyteachers.get_underpaid(limit):
        x['salary'] = num(x['salary'])
        count += 1
        r += '<tr class="success"><td>'+str(count)+'</td><td><a href="teacher-%(id)d">%(first)s %(last)s</a><br /><small>%(title)s</small></td><td>$%(salary)s</td><td style="text-align:center">%(rmt_overall)d&#37;</td></tr>'%(x)

    r += '</table>'

    return r


def table_highestpaid(limit):
    return table_highest("salary","Top "+str(limit)+" Highest Paid Teachers","Salary",limit)

def table_highest(param,table_title,column_title,limit):
    r = '<table class="table table-bordered"><tr class="active"><th colspan="4" style="text-align:center;">%s</td></tr><tr class="active"><th>&nbsp;</th><th>Teacher Name</th><th>%s</th></tr>'%(table_title,column_title)

    count = 0
    for x in stuyteachers.get(param,-1,limit,0,True):
        x['salary'] = num(x['salary'])
        count += 1
        r += '<tr class="active"><td>'+str(count)+'</td><td><a href="teacher-%(id)d">%(first)s %(last)s</a><br /><small>%(title)s</small></td>'%(x)

        info = str(x[param])
        if param == "salary":
            info = "$"+info
        elif param == "rmt_overall":
            info += "%"

        r += '<td>'+info+'</td></tr>'

    r += '</table>'

    return r



def searchCode(a):
    a = {}
    if "name" not in a:
        a["name"] = ""
    if "title" not in a:
        a["title"] = ""


    r = """
<form method="get" id="searchForm" action="stuylist">
  <h3 class="form-search-heading">Search for a Teacher in Stuyvesant</h3>
  <input name="name" type="text" class="input-lg search-query" placeholder="Enter name" value="%(name)s" autofocus>
  <input type="submit" class="btn btn-lg btn-primary" value="Search" />
<!--
  <br /><a href="javascript:void(0)" onclick="$('#adv').slideToggle()">Show Advanced Search Options</a>
  <div id="adv" style="display:none">
   <table>
    <tr><td>

<strong>Filter by title/department:</strong><br />
<input name="title" type="text" class="search-query" placeholder="Ex: Physics" value="%(title)s" />

    </td></tr>

   </table>
  </div>
-->
</form>
"""%(a)
    return r




def table_get(param, sort, limit, offset=0,teachers=False):
    sort = int(sort)
    offset = int(offset)
    return table_get2(stuyteachers.get(param, sort, limit, offset),offset)

def table_search(ar,limit,offset=0):
    sort = 1
    offset = int(offset)
    
    return table_get2(stuyteachers.search(ar,limit,offset),offset)



#def table_get(param, sort, limit, offset=0,teachers=False):
def table_get2(loop, offset):
    # teachers - if True then ONLY TEACHERS appear (no guidance, administration, etc)
#    sort = int(sort)
#    offset = int(offset)

    r = ""
    if offset == 0:
        r += """
<table class="table table-bordered table-striped" id="sortTable">
  <tr class="active"><th colspan="12" style="font-style:italic;text-align:center;">Click a column header below to sort</th></tr>

  <tr class="active">
    <th colspan="5" style="text-align:center;">Teacher Information</th>
    <th colspan="7" style="text-align:center;">Neighborhood Information</th>
  </tr>

  <tr class="col_heads active">
    <th>&nbsp;</th>
    <th><a href="javascript:void(0)" onclick="sort('last',1)">Name</a></th>
    <th><a href="javascript:void(0)" onclick="sort('salary',-1)">Salary</a></th>
    <th><a href="javascript:void(0)" onclick="sort('rmt_overall',-1)">Overall<br />Rating</a></th>
    <th>Address and Phone Number</th>


    <th><a href="javascript:void(0)" onclick="sort('zip_MedianIncome',-1)">Median<br />Income</a></th>
    <th><a href="javascript:void(0)" onclick="sort('zip_MedianAge',-1)">Median<br />Age</a></th>
    <th><a href="javascript:void(0)" onclick="sort('zip_CollegeDegreePercent',-1)">College<br />Graduates</a></th>
    <th><a href="javascript:void(0)" onclick="sort('zip_AsianPercent',-1)">Percent<br />Asian</a></th>
    <th><a href="javascript:void(0)" onclick="sort('zip_BlackPercent',-1)">Percent<br />Black</a></th>
    <th><a href="javascript:void(0)" onclick="sort('zip_HispanicEthnicityPercent',-1)">Percent<br />Hispanic</a></th>
    <th><a href="javascript:void(0)" onclick="sort('zip_WhitePercent',-1)">Percent<br />White</a></th>
  </tr>
"""

    count = offset
    for x in loop:
#        if not teachers or "Teacher" in x['title']:
        if True:
            count += 1
            r += '<tr><td>'+str(count)+'</td><td><a href="teacher-%(id)d">%(first)s %(last)s</a><br /><small>%(title)s</small></td>'%(x)

            if x['salary'] != -1:
                r += '<td>$%s</td>'%(num(x['salary']))
            else:
                r += '<td style="font-style:italic;">No Data</td>'
        
            if x['rmt_overall'] != -1:
                r += '<td style="text-align:center;">%(rmt_overall)d&#37;</td>'%(x)
            else:
                r += '<td style="font-style:italic;text-align:center;">No Data</td>'

            if len(x['address']) > 0:
                r += '<td><strong>%s</strong><br />%s'%(x['address'][0]['address'],x['address'][0]['phoneNum'])
                if len(x['address']) > 1:
                    r += '<br /><a href="javascript:void(0)" onclick="viewmore(this)">[Show '+str(len(x['address'])-1)+' other possible addresses]</a></td>'


                if "zipinfo" in x["address"][0].keys():
                    pk = x["address"][0]["zipinfo"]
                    r += '<td>$%s</td><td>%d</td><td>%.1f&#37;</td><td>%.1f&#37;</td><td>%.1f&#37;</td><td>%.1f&#37;</td><td>%.1f&#37;</td></tr>'%(num(pk["MedianIncome"]),pk["MedianAge"],pk["CollegeDegreePercent"],pk["AsianPercent"],pk["BlackPercent"],pk["HispanicEthnicityPercent"],pk["AsianPercent"])
                else:
                    r += '<td colspan="7">No Information Found</td></tr>'

            else:
                r += '<td colspan="8">No address found</td></tr>'

            if len(x['address']) > 0:
                r += '</tr><tr /><tr style="display:none" id="addr'+str(x["id"])+'"><td>&nbsp;</td><td colspan="4"><table>'
                for y in range(1,len(x['address'])):
                    r += '<tr><td style="font-weight:bold;">'+x["address"][y]["address"]+'</td><td style="padding-left:15px;">'+x["address"][y]["phoneNum"]+'</td><td colspan="7">&nbsp;</td></tr>'
                r += '</table></td></tr>'



    if offset == 0:
        r += '<tr id="loadMore" class="active"><td colspan="12" style="text-align:center;"><a href="javascript:void(0)" onclick="loadMore()">Load More Results</a><br /><br /><a href="#">Back to Top</a></td></tr>'


        r += '</table>'

    return r
