# groups begin with { and end with }
# garbage begins with < and ends with >
# groups can be within groups
# inside garbage, any character that comes after ! should be ignored

emptyGarbage = {
            '<>':'',
              '<random characters>':'',
              '<<<<>':'',
              '<{!>}>':'',
              '<!!>':'',
              '<!!!>>':'',
              '<{o"i!a,<{i<a>':''
                }

numGroupTesting = {'{}':1,
                   '{{{}}}':3,
                   '{{},{}}':3,
                   '{{{},{},{{}}}}':6,
                   '{<{},{},{{}}>}':1,
                   '{<a>,<a>,<a>,<a>}':1,
                   '{{<a>},{<a>},{<a>},{<a>}}':5,
                   '{{<!>},{<!>},{<!>},{<a>}}':2
                    }

scoreTesting = {'{}':1,
                   '{{{}}}':6,
                   '{{},{}}':5,
                   '{{{},{},{{}}}}':16,
                   '{<a>,<a>,<a>,<a>}':1,
                   '{{<ab>},{<ab>},{<ab>},{<ab>}}':9,
                   '{{<!!>},{<!!>},{<!!>},{<!!>}}':9,
                   '{{<a!>},{<a!>},{<a!>},{<ab>}}':3
                    }

puzzleInput = '''{{{{{<!!!>},<!e!!!'ue!o!!!>"oo<u!}<<{>},{{{}},{<!>},<'>,{<!!"!!!>"u!!!>!!!>,<"!>,<!>},<}!!}!!!>{>}},{{<"!>}}!'!!u!!!!e!!!>>}}}},{{{<!>>}},{{{<{{!!,>},{<u!!e'!>},<>}}},{<,o!!!""a!>},<!>},<<}>,{<!!!!,,!>,<!>},<"!!!>u>}}},{{{<}{!<{i!>>}},{{}},{{},<!>,<!>,<!>!!,<!!!!{}!!i>}}},{{},{{{}}},{{<ae{>,{}}},{{<!!!!">,<{'}!!},<!>a,!>!!!>{!!e>},{{<!ao!!i!'!>,<!!o>,<'e}!!!>!!!>e'!!u{>},<",'i!!!>{>},{<uai,!!{!>},<uu!!e>}}},{{{{{<!!,a!>>}}}},{},{{{{{{},{{<au<,!!iuu!!!!!>,<>}}},{<i!>,<!>},<!!'iu{!!o"{i,i}!{{>}},{},{{<a!>a"!!!!!>},<>,{<!!!>">}},{{{{<ae}a!!!!{!},u!!o<!!!">},{<!>,<!!!>!!!>},<ee<!'!>},<!!!>u"ae>},{<e'!!!>},<'e!>>}},{<u!>},<a!>!>i,u>,{<i,!!>}},{<'>}},{{<!ee!>},<!!!>!!!>>},<!!!>},<a!u>}}}},{{{{{}}},<!!!>>},{}}},{{{{<!>,<,,},,!>,<<!!!!<<!!<!!!!>}}},{{},{}},{{},{<o,!>},<!!}!,!>},<o!>uoa{<a!!,<a!>,<>}}},{{<'!>},<e!>>}},{{{<!>"<e!!!>}!!!>!>u<'i!!}'!!!>>},<ie!>a{!{>}}}},{{{{<{i<!>}e!>},<}!!,,!>},<!!aa!>a!!!>!,{>,{{<ii!>,<>},<{e!!!>"!!o!>,<'a!>},<u!>!>>}},{<!!!>"!>,<!<!>,<u!!!!i!>,<a!eeu!!!!!>!!e>}},{<i,}a!!{e>}},{{{<}eue!a}{"{''<!,!>'!>},<">},{}},{{}},{{},{{{}},{<'!!,ie"e!!!!!>">}}}}},{{{<!!<<!!!>o!!!>eie<!!!>e!>"!!!!!!ie>,<!>!>!,!!u!!o!!!>!!!>,<'"!!u!!}u}<}!>,<}>},{<!,!>},<auo!!!>!>,<{}!>,<!>,<>},{<>,<<!>},<{>}},{{{<a!>},<i!!!!!>!!e!>u>,<!>!>},<!>},<a!>!!!!!!i<ae{<!>,<!><o!!!>!io>},{{{}}}},{{<{,ii!!!>!>,<i'{uo!!!>{a!e>},{}}}}},{{{{{<!>,<u!>!!!!a",!!,!><!!!!!>,!>,<i">},{<"!>,<!!'>}},{{},{{<!!!>!!!>>},<>},{{{},{}},<e{!!!>!!!><u!>},<iioi!>,<!>!>},<o!!!>!<!"!>>}},{<<<!a{!e}!!'!!<!>},<!>,<'eoiua}'>,<!!<!!>}},{{<!>>,{{<!!!!!>}!>!!a<!!u!!!<u"!!!>>},{{{<!!!>"i!!ae<!><i!>,'>}}}}},{<!>!>i!>,<}!>!u<!!!!!>!<'o!>u!!!>!>e>,{}},{{{{<!!a'!>},<!><{u,}""!o!>},<!>,<>}},<!!!>,<!o!>,<!>,eea,!!!>i,,ue,ie>},{}}},{{<'e",!!!>!>,<!!'!!!>'!>{i!,!!!>},<''!>>,<!!,!>},<}uu!>"a"}!!<!>},<!>,<!>}o!!o"'>}}},{{{{},{<!!,!!a>}},{},{{{{<"uo!!!>!>,<"!>e,<',au'}>,{}},<u!>},<!><a}'ei!>"!!}a!!!>,<!>u<u>},{}},{},{{<}"!!e!>,<{!!!>!!,!e"!>},<!>},<!!!>,<!'e>},{{<!,iuee{u!!!>i!!!>{<!!!>},<!i!>},<!!>}}}}},{},{{{{{{<!!u!>},<o>},{<!!!o!!,>}},{{{},{<i,'<a!!"}!>>}},{<}a"u!!"'!!<!>,<!'!!'"uai!!!>},<>},{<>,<}!>!>o}}!!o{!>},<>}}},{<!>},<!!!"!!!>a!!!>!>},<!>}!>,<>,{<{!!e!>,<"!!u!!!>"!!!>!a!!a<oo"!!!>!>i>}},{{{<!}!>},<}u!!!>!!!>!>},<!>},<>}}}},{{<}!>,<a,"o<!>!!!!!!"<!!e'a'}!>},<>},<!!!ee,'<}e!<!>,<i'!!!!!>u!!!>,>},{{{}}}},{{{<,>}}},{{<o,!!!>!>,<>}}}},{{{{<u!!!>>},{{<'i!!!!!>,<!!a!>,<}e<!>,<'>},{}},{<{<!a'>}},{{{},<e!>,<<e!oou!!!!!!"!!i!!!!'a!>},<,!>,<<>},{}},{{<!>,<!!e!>!>},<o<!>!!!!!!o"{!>},<>},<,i{i!>,<oaue<"e'!!u{ue>}},{{<e>},{{},{{{{<e{oi!>,<o!!!!u>}}},<e<!ue!!oo{!>,<a{!u<!>,<"}i!!">}}},{{{<!>},<!!o!!e!e>,{<}!!{{!>,<!o!!ao}{{!>,<>}}},{{<o'>},<,u!!o!!u>},{{<>},<'!>,<i!!!>},e!,e!!{>}}},{{{{<'ao>,{<!>!!""!>!u!>,<i!>a!,{u!!i!!!!!>>}},{{{{<!>},<a""oi!>"'>}},<a<e{,,o!!"!!!><>}}},{{{{<au<!!!!!>!>,<>}},{}}},{{{{<oa!!!>iaui!,!!}>},<ia!>},<u'u!!!>!>u>},{<"u{""u!,!!!>>}},{<!o,{!>a!o''!u!>,<!!!>},<!!o!!!!!>,<>,<}<,!!o!>},<}{}{!>},<{">},{{<!!}}!>,<!>!{e<"!!,!>,<">,{<'!<!!u!>},<!!!!!i!!u,"oo!!!>!!!>'a}">}},<!!'u!>},<au!>},<!!!>!>,<>}}},{{{{<a!>,<'!>,<>},<!>,<<o!<!!!>,<!!i!>!"i!>},<}>},{{{<o}!>>,{<!>>}},{<!!!!!>!!<e!!<e<,!{!>,<>}},{<!!!!eo'"!>,<}<}!o<!!!>{u>,{}}}},{{{}},{<"!>!ai!><'e!'!>!>>,{<u!>,!>!!ae!!'e!!!>e>}},{{<!}!!u'e{i!!'!"!!'<!!!>,<>},<o'a,'e!>,<{{aau!<{u>}},{{{{{},{<e!!"i!>!!!>u!!"""o{!>},<!!o>,{<}!!>}}},{{<'}o,ie">}},{<!!'{!>},<ue!>,<!!!>!!ia!>,<">,<a,<ouu"a>}},{{{{<u!>,<!>},<e!><!!!!}}!>,<!>},<}a!>},<i!!'!i!!!>a>},<!"u!!i"ioe!!!>!!,!!ie,!>o"!>,<!>,<!<>},{{},{<o!>},<{a!!!>"{>}},{{<iu{}"!>,<"{!>i<o,e!>,!<>,<<!aa>}}},{{},{<i}!!!>>}},{{<a!i,,!e<!>},<!"i'}"!>{ii!!!>!!,>},{<u,'!e!!!!'!ee!!"!!i!!!>},<}>}}},{{<!!!>!!u!>,<u!>"o<<}!>uu!!u{!!u!"!!!>>},{{<!'!>o>},<i{ioeu!>},<{au!!!>!>},<i!>},<!>,<!>},<!!!!,e>}}},{{<!!!>},<!!!>i<o!!}}e!,i!>o!!!!i>}}}},{{{{{{<!>},<>,<'e!a!!!o}}<"!!!>,"}!>a!!!>"e>},{{<e!>!!{"},,!>,<!!'!!!>aa>},{}},{<!!,,!e!>!>},<!>,<"{"!!!!!!!!!>>,{<"!!!i!>},<o{""}",,!{ou!!>}}},{{},{{<!!!!!'!>{oe<{!!<!!!!!!'>},{<!>,<<'e!"!>!>},<!>},<{!!o!>,<e!>!!u}!!e!!>}},{{<}o"!>},<!>},<!>!!<!u!!!>},<!>},<i!a>}}},{{{{<'!,!!!!ii>,<<!{!!!>!!!!!>!>},<!!!>!!'!>,<o{iuo!><!!o}!!!!!!!!!>!!!>>},<!>!>,<!>ao!!!!!>!>},<<!!{"e!!,!!{'!!!><>}},{{{<!!!>,a!>},<!!!>>},<!!!>!!>},{<!!!!<!>,<,>},{{<}!}!>,<o!!!!!!!!!>!!!>'!!a!>},<>}}},{<>}}},{{{{{<!>,<!>,<!!!>},<i!>"!>},<o<!!!>a!!!>!!!>!>!!,u!>>},{<<""!!,!>},<'{<!o>}}}}},{{{{<}!>,<o!>,!>},<!!!>'i",!>},<!!!>,<{!>,<o!>,<!>},<>,{<<!>!>,<!!!>!>},<>,<!!!!a!!a}{{!!!>'!>,<{<<!>,<>}},{{<!!,>},{<!>,<!!ao!!!>!>!!!>!>},<,i{o!!!>"!!e!>,<!!u>}}},{{},{{},<u!>,<!!!>!!>},{}},{{{{<}'e,}>},<>},{{<e!i{!!!>!>},<"!>},<!e!>,<{>}},{{<>,<{{!ei'!>},<<{!>,<a!>!!">}}},{{<!>,<{!!{}i!>,<{!>"<!>,<!>!!!>!!!!!>!ou>,{{{{}}}}},{<{'!'<}}>,<a>},{<{{a>}},{{{<>,<!!u"!>},<!>u!!!>'>},{{{<a!>},<o!>},<'!!!>o!>,<!>,<{u!!{!"{!!!!!>>},{<,<!>{!a>}},{{<}>},{<!eu<!>,u'!>},<!!!><e{e!!!{<!!!>!!!>>}}}},{{{},{<a!>,<<e!>},<!!!a<u!!!>},<!>,<i!>,<>}},{{{},{}},{<!!,!!!>},<ia!!!!!>,<!a!!!>},<i'!>,<!!!>!>},<>}},{<'a,!>,<!!!>!!!>,<'!>,<<"u>}},{{<!!!>"u!!!><'!!!>{>},{<'!>,<}>}},{{<i!!{!!!>!!!!i,!>!!<u,u!>},<'!>},<ao,"!!>,{<e!!<'e}<!o!>{!>!>!!!!"i>}}}},{{<!>},<!>},<}!!!>"!!<!!!!!>e>,<!>ia!>,<!>"!>!!!>i!!!!!!u!eu"a!!,!>},<>},{<{o!>,<<"{!!!>!!o!>},<!"a!>>,{<<e,!}ao!>ui<!>!>},<'e<!!!!{a!>!>,<>}},{<>,<',!>iaoi!u<oe"!>>}}},{{<!>e"e!!!>},<,u!!e!>,<!>,i!!oi<>}}},{{{},<!!u!>!!!>i!!!!e!!,"u>},{}},{{{},{{},{<!>},<!a>}},{{<"o!>},<!>},<!!!>,<!,>},{}}}},{{{<!>!ei!!{!!<!!>},{}},{{},{<io{!>},<!!}!>},<!}a!>u<>}}}},{{{<!>!!!>"!>!!ua>},{{<!!!!!>{!">,{<!!'<"'!!!>}!!!!!>!!a!!'!o',!!!!!>!!>}},{{<!!"!!!>{{,!>,<!!!>!!i!!ea!!!>!!!>'>,{<!a<!>},<!>,<eoe!"!>e<a!!}"e!>},<o!!>}}}}},{},{}}},{{{{{<!>!{!>i}!"'!!!>iau!>},<o>}},{},{}},{{{}}}}},{{{},{<!>,<!!u!>},<!!!!<<!>,<!>auo!>">}},{{{}}}}}},{{{{{{<!>!>},<!!!>oe!!!!'!>},<"!!!>>},<!>{!!"'!>,<!>},<oe''{'!>,<>},{}}},{<u!e}!>,<!<!<!<"!o!!'!!>,{{}}},{{<uia!!ee!>},<!>e>}}},{{<o!''e>,<!!!>eu{"!!}a>}},{{{{<!!!!!>!>},<!><o!i>}},{{{<!!!>,<io!>,<o}ou!>,<!{!>},<!!ou!>!!!>!>,<!!>},<!!<'!!!>,u,!>o}"!a>}},{<!>'!!{eo'!>},<!>!>,<e!!a!!!>!!!>{,,!!!">,{<"ioau}'!!!!!!!>!!!>i">}}},{{{<{!!uo{i!>},<,}>}},<ie<{u<!>},<!!"i<>}}}}},{{{{{<!!!>!!i>},<>},{{{<!>},<{!!,!!a""i!!}{>}}},{{{<!>},<!>,<a!!!>,}!!!u"e!!!o>},{<!!'{!!!>,<!!'!>},<!!!>e,!>,<e'!!!>oo>,{}},{<}}!>},<o'!!!>!!!>!>},<ee!!"<!,>}},{{<!!!>u{!!e>},{{<!o!>},<e"}u!"!!}a!!a{<,!!ee!>}>},{{{{},{<!{u{!',u!!!,>}},{<"'!!!>!ae'a!!!!o!!!>a!}!>,<>}}}},{{<!!!>o"i!!!>"!!!!!!!>!!!!!>},<}!!>},{}}},{{<'!>,"!!!>},<oo!o'!>},<o>,<>},{<auu{<!>e!>},<!!!>}'>},{{<}"u!!!>!!,"i!>e>},<",u>}}}},{{{{<!>,<{"!!a!>,<"ou!!,a!!!>},<!!!!{>}},{{{{<!!!>,<o!>!!!!eue{!>},<!!u<>,{<>}}},{<!!<{!!!>oo!!u!>,<!!!>!!!>,<!<>}},<"eo<!!!>"!,!!!>>},{{}}},{{{<>}},{<a,!>!!!>!>},<<!>},<}o!!!>uui,"!!"i}>},{{<!!!>!!<{<!>eu!>,<a!!>,{{{<i'eua!!!>!!!u!!!!!>!o!>,<!i"e>},{<io'}"!>,<a!<!>!"}o'!!!<!!>}},{<{e!!!>!!!},!>,<"">}}}}},{{{}}}}},{{{{<}!!!>eo!!!>a!e'>,{<ui!!!!!!!!a!!!>!">}},{{<u}'!!i'ueo!>>},{<u>,{<o!>},<i!!{!!!>}!!<"u!!!>},<>}}}}},{{{<>}},{<!!!!!>!!{<aoo!>},<!!'ou>},{{},{<!>},<}!>,<u,"!!!>e}!>u!{o{!>,<!!ae>,{{<!>},<o!>,<!!o>},{}}}}},{{{{}},{{<o,{!!!>!>!!{!>},<,>,{<}e,!!!>>}},{}},{{{<{!>,<!!!!ai>},<!>,<i>},{<!!!>!>,<!!,!i!>!>,<'"!>!'!>!!i,>}}},{{{{{<a!>,<u{{!!!o!!{ua!>,<!!"!}"!!!}!!!!',au>,{{<!!{{!!!>>}}},{{{{<i<o!!i>},<ia!!!e!!!!!><!>,<i!!!>}!>,<ii<!!!!!>>},{{{<,!!!>,<!!<>}},{{{{<!!!!!>},<!!i!>,<!!e!>,<!!!i{<!>!!!!!>!!!><e>}},{}},{<!!e!uui"<{!>,<>}}},{{<!>,<!!!>{,aa!!u!!o!!{u>,{{{<{!!!>>}},<!>>}},{<,!>},<!>,!}"!>}!>},<"i!!!>>}}},{{<!!!>u!>},<i!>,<!>},<!!!!"!!!!"ee!!!!!>!>},<o!<!>},<e>,<e!!!>"!>!!e!>,<',!!>}}},{<a!!}o!!!{{o"e!u!>,<a>}},{{<}!>},<}e}!!!>!ua'>},<!>ooe,u'!!!'>}},{}},{{{<o{,'!!!>o""'>,{<!!'e!>,<oi,!,>}},{<'!!!>,!<<a!>>}}},{{{<,o!>,<!>},<!!!!!>,<}a,!>}!>},<iei!>,<!!>}},{<{{,!>,<>,{{}}}},{{{{{{<!>},<e,<!!u!>},<a!!!>''!!!,'o!{>}}},{<!!a!>,<{!!!!""!!!!!>'!!oa{{!>,<!>},<>,{<",!!!>!!a!!!>},<e!!!>!!"ii<a!>,<!"!!>,{{<'!!!!!>!>},<e},>},<!!<a!>,<"!!!>a'!!!!<'>}}}},{<i!'!>!!!>},<,u'u!>},<i!!i!!!>,<<,!!!>oai>,{}},{{<u>},<!<ea,>}},{{},<{!'<!a!!!>!>,!>{!!!!!>u!!'>}}},{{{<>},{<!!!>"{o!!!>!!!>},<!!!,>}},{{{{{{<{!!a{<<a!!!>!!!>!!!>,<!!!>!!!>>,<}"e,!oae''!>,<!!{u!>},<!!}!>},<'>},<}!>,<<{a!!uo!>!>,<!>,<!!ei!>},<{>}},{{{<,"i!>,<i!>!!!>o!oa!>,<!"!au'iau>},<!>,<uiu!!!!!>}ao"{u!!!>'!!!>a>},{<!o!>,<,i!>,<!>},<u!!a!!!>},<}!!!>u!>},<!!<o>,<!!ei!>},<!!!>!!!>},<{"!!!>,<<!!!>u!>!!!>!>},<a>},{{<{!>'!!<"!!!!>}}},{{<>},{{<!!!>e!>,<!!<o!!"o{,'<!>},<!>}>},<!!}!!>},{<'!!a!>},<!!ioiau'u,!!!!!!,!>},<i!!!>{>}}},{},{<!>},<!o">,<!!!>}!!!!!>!>},<"!>},<!>,<>}},{{{{}},{{{{}},{<i!!<,!!o>}},{{},{<!>},<!!!{u{!!!>a!!!!i!!,'!>},<}>,<"'!>'>},{<i>}}},{{<!!!>!"a!>,e<i!!!>,<,!!!>!>>}}},{{<!>,<!"{!>"!>,<<o<ue{{}}!>,<!!>,{<u}>}},{}},{}},{}}},{{<!<!>{'au!!"{!>,<>,<!{>},{{{<e!>u!{'!o{'!!!>!!"!}!e"!>},<oiua>}},<,!>,<!e">},{{{},{<!!a!>}!!!>u"!a<!>,<,"{!>},<a<!>,>}}}}},{{{<!!,!"}!>}!!}!>,<!}""!!e,}!>},<>,{<,!>},<a,<u!!!>!!}}e"!}>}},{{{<a>,{<<e!!!!u"auo!>u!>,<>}}},{{<!"<!!!>{u!>,<e,{{!!!!"!>,<!>,<,}!"'"e>},<<!>},<oua!!u,<<>}}},{{{<eu"!>u'uu<>}},{},{{},{<!!!>!!!!u}iio!>>,{{<oo!!!>{!>,<{!!!!!>,<i,!!}}!>u!>a!>,<!{'>},<!>},<a!!!>!}!,ea>}}}},{{{{<!!i!>,<!!!><u!!a!!!>,<>,{<!>!>}!!o!!!><a<>}},{<!>,<!!'{i!!a!a'<!}!!e"!!!!a!>"!!!><>},{<!!!>},<!!!>,<!uea!>},<'!!>}},{<!>,u{<!>},{!{iie{!>},<<o!>,<>,{{<!!!>!!}iu'!!!>e}!!!!o!><!>!!!>,<<!>,<!!!>,<!!,>}}},{{<"i'{!i!>a!!{!>,<oaa!a!>},<>},{<!>,<o">}}},{<!!}!!e<e>,{}}},{{{},{<">}},{<!!!!"!!o!!!>"!!!>i">},{{{{}}},{}}}}},{{{{<i'<u!{e{i>}}},{{},{{<o>,{<!!<}}{{o!!a}!!!{ao>}},{{},{{},<uu'!},!!e!ouu<oia!!!>e}{e>}},{{{<<,e'a!!!>},!!!!!>e>}},{{{<o!>},<uo!!!>!>!>,<u,!a!!!>!!!!!>}!>,<!!!>>},<!a}i,">}},{<!>,<!!,!>}!!<}!!!!!>ae<u!>,<!>,<!!!>!{<!!!!">}}},{{{{<!!,,!>},<i}<{>,<!>,<!!{}o!!{,<,,!u!"!>,<>},{<}!!!>>,<oo<!>},<<ou}!!!>}e!>,<!>,<>}},{{{},{}},{},{<uou>}},{{{<!>!""<ea>},{<<i!>},<'aau!>},<!>,<}i'!>!!>}},{{<e"!>,<{"!!!!!!!!!>,<<eui"!!},!!>}},{{<'i!!<>,<!!!!"!>,{<!>!!{!!!!!!a{!>},<>}}},{{{},{{{{<!>!>},<>},{{}}},{{{<''!!!>ai!!a!>!>,<>}}}}},{{<a!>,<!!'a}<,!!!>},<,!!,!}!>},<>,<!!!>,<{!!!>!!io!e!>,<!!!!!>,>},<!{i!!!>,}'{o!!,<!>},<!>!>!>},<oie>}}}},{{{{<,,!!i!>,<!>o!>,<>},<}!!!>},<e!>,<}!!>},{{{<!!!{oo!>,<!!!>!!!>,<o!!!>e>}},{<!!{,!>!!!>!!<!>},<!!!>!>,<i'!!!>!!!>},<'!>,<>}},{<a!>,<!!!!i!a'o!!!>u!!!>i>,{<'u!!}oe<!>!e!!">}}},{<i{!!o">,<!uo'}!!!>!!!!!!ou<!!!!!>}a>},{{<!!!!"{}>},{<uoeua!>},<o!!!>!,i">}}},{{{<!!!eo{>}}},{{<!!{!!'ui!!!>!>},<>},{<a"!!!<o>}}}},{{<,u'!{!!'!>!!!>}>},{{},{<,!!!!!>},<e!!">}}}}},{{{{{<!>,<!!,>}}},{{<!!ouao"!!i<>,<!"!>,<!!oe!>,<i}ei!"{!u!>},<,>},{{{}},{<<!>,<>},{{<<<,u!!",!"'!!!!!!<a{u!><!u}>,{}}}},{}}},{{{{<!!!>o,!!!!<uu!}!!e'uu!!"e!>!e!>,<!!>}},{{<>,{<u!!!>,<,!i!!!>""u!}}!!!>!<e"!!!!<!!>}},{<u!>},<}{!!!>,<o>}}},{{},{{<!!!!!!u'!>},<,!>,<!!a!!,iu>,{<!{!!!!}>,{<ei!>,<}oo>}}},{<!>!>,<!uo>,<>}},{<o{"<"i}{!{{eae>,{{{<!!!e>}}}}},{{<}u!a}!!!,!,"e>},{{<>},{{<"!>,<ao'}!>,<!!!>,!>"eu{i!!}!>},<,>},<!{!>},<!!!!{{!!!!!>!>"!!<!!!!>}},{{{<u!>,<u!!!>u!!'i>}},<!!!>ii!!!>}{!><{!>e'!!!!!}{}!>!io!>>}},{{{<>},{<ua!a!>!>!!<!!!>!!!>,{u>}},{{<>},{}},{{<!>!>,<au{u!>,<>},{}}}},{{{{<,!!!>i!>},<'!!!<!!!>u!!!>i<!}!>},<!!!!e>}},{{<u"!>i!'>},{{{{},{{}}},{<!!!>!!}!>,<o<!!!>},<<e<i<"}""!>,<!>,<'>,{<'"i!!ae{o}!>!,a>}}},{<!!!><!uu<!!{!>,<}}'!o!><{>,{<!u{!u!>!>},<'a"a,!>},<!!}{!!,'ei>,{{}}}}},{<{i!!u!>},<!>},<!>!oo>,{<e{u}<,!!!!!!i'o{<!!!>!!'i'uo>}}},{}}}},{{{{{{{{<u,<!!<i}a!>!>,<e<!>},<,i!o!>,<>},<u!!!>,oii,!>},<}}!}<e>},{},{<i!>!!i!>e!>},<!>!>},<>,{<!!!>ii}<!!!!!!e{!!!>",!!!e!>,<u<>}}},{<>},{{<a}!!}i!>,<io<i!>},<{!,e'!!!>,<!!!!!!!>!!iu>,<!!!>o!!u,!>!>,<!>,<"i!!e!<e">},{<!!,{{!!!>'>}}},{{{{},{<!!!>!!!>',oao}<!{!!{!o>}},<!><!>,<e!>,<o!!!!ou!!!!!>},<!!!>>},{{}},{{<!>!!!>"!>!!i!!!>!!!><!!!><!!!>i!<!!!!<{!!!!!!!>e>,{<,,>,{}}}}},{{{{<u,!>{uu>},{<>}},{},{{},{{<"e!!i<!!!>,<"o!!!>,<}u>}},{{<>},{<!><>}}}},{{<!!i<!!>},{{<!>,<!>},<!!!>!!,e{>},<eu"!!}u}!>},<<a>},{{}}},{{{<!i!!au!>},<,!!!>},<u"<,{{!!,!!>},<a{!!!>>},{{{<e!!!>a!>,<}e!!!>{>}},<!<!!oa}!!'"!>},<'u>},{{<,ua!!aoo}!!{!!!!!>!!"eau}}!><!!!>>},{<!!!!!!>}}}},{{<!!">}}},{{{}},{<,!u!>!>,<!>,<''!!!>!>},<'a'!!aou!!!><>,<u>}},{{{<i!>,<!!i!!!<aa!!a>},{<!>,<a!>},<!!!><!>,<a!>},<!!u!>!!!>""!>,<!!}>}},{}},{{<o!!o>},{{{<{!i!!!!e<ua>},<>}},{<!!!>!!!>'!!",e}u!>},<!!'!>,<!>,<>,{<'e!}!!<!>,<i!>,<"o!>>}}}},{{{<u"!>},<{!!'u>},<!>,<<!!!>!!'!>!!!>,<u'<}'!>,<ee"!>,<a>},{<!!i>,<o!>,<!iu!>},<!!'o<}!>,<,">},{<<{!>},<<!!!>}'!!!!!!!>!!'!'o!,!!u>}},{{{<!!oi'a"!>"!u}!>,<u!>},<"u!>!!">},{}},{{<!>},<eae!}!!!>aa!>oa!!o!!!>!!}<u}>,{}},{{},{<!!!ae}<!!,!!!!{!,u!!<!!,!!!!!>!>},<>,{<'"!>!!!,u!!oo!>,<>}}},{{{<!>},<!>!>},<}!!!>a<"{a!!!>!!<!>,<!{!!!!!>>},<{>},{{<!"!>,<"!!!>>}}}},{{<}<i!>eu}u!>},<iii!!}o>},<aa"u>}},{{{{{<<!!'!>},<!!!!<!>,<',{o"{'!!i>},{<!!!!!!<e!i"},!}uua<>}},{<i!!a'{>},{{{<{!e<!}!!!>,<'o{>},<o!!!!!>{!>},<!!!>e!"{!>},<{!!'u!>},<ioia>},{<!!!!u!{<!>},<'>}}},{{<!>},<!>},<,au!!{>},{{{<!!'<!>,<<!>>}},{<!!!>!!!!!>},<!>,<ueie!>,<!!i!>},<>}}}}}},{{{<e!>!!u!!!>!>},<u<ua!ao>},{},{<a!!e!>u,!>,<}}!!!>,<>}},{{<}!>,<'>,{<o">}},{<u!>!>!!oi!!!>"o"!!ie{>,{{<!!!!!!,!!!>,<!!u">,<}!>},<}!>,<a!>"!>,<!>!!!>!!!>},<!>,<e>}}}},{{{<o!!!>a!>},<!>,<}!!!>},<!}!!!!!>!>},<o!',{>}}}},{{{{<"!e"!!!>!>,<!!!>!>,<o,'ai!,!>,<>}},{{},{}},{{<!,,a',!>'o<eu}e!!!>,<!!!!!!!>ia!>},<!!}>},{<o!!!>,{<"'!>},<>}}}},{{{{}},{{<!>,!>,<a'!>},<ee!!!>io>},<}!!!>,<!!ee"e!!!>'}!>},<,!!!!aa>},{{<!!!>},<}!!,o!i,!>,<!>},<}<}!>e>,{<<!>},<"!!<>}},{{{{<!>},<}o!!"!>>,{<!>},<!!!<'!>},<>}},<e!!!>,<!!!>e!>,<'!!!!!>!!!>,>},<i!,u!!!!!}!>},<!}'"!>o!>,<u!!!!!>>},<,!!!>u<!>>}}},{{{{<a!!{!!o'!}!!o!!!>},<{a!>a>},<!>},<eu!>,<"i!!!>i!ai<>}},{{{}}}}}}}'''

def cleanupGarbage(stream):
    i = 0
    score = 0
    outStream = ''
    inGarbage = False
    while i < len(stream):
        if inGarbage:
            if stream[i] == '!':
                i += 1
            elif stream[i] == '>':
                inGarbage = False
            else:
                score += 1
        else:
            if stream[i] == '<':
                inGarbage = True
            else:
                outStream += stream[i]

        i += 1

    return outStream, score

def groupStream(stream):
    groupDepth = 0
    score = 0
    for char in stream:
        if char == '{':
            groupDepth += 1
        elif char == '}':
            score += groupDepth
            groupDepth -= 1
    return score

for stream in emptyGarbage:
    cleaned, garbageScore = cleanupGarbage(stream)
    if cleaned != emptyGarbage[stream]:
        print('fail', stream)
    #print(stream, garbageScore)

for stream in scoreTesting:
    cleaned, garbageScore = cleanupGarbage(stream)
    score = groupStream(cleaned)
    if score != scoreTesting[stream]:
        print('fail ', score, ' ', score)

cleaned, garbageScore = cleanupGarbage(puzzleInput)
score = groupStream(cleaned)
print(score, garbageScore)