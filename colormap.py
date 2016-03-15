try:
    from collections import OrderedDict
except ImportError:
    from legacy.ordereddict import OrderedDict

# example color maps
userid_pat_to_color_default = OrderedDict(
    [
        ('[a-z][_a-z0-9.-]*', 'Gray_L'),  # catch-all rule for many more names
        ('Atlassm', 'Red_L'),
        ('sgmatlas', 'Red_L'),
        ('patlas', 'Red_L'),
        ('satlas', 'Red_L'),
        ('satl', 'Red_L'),
        ('atlassgm', 'Red_L'),
        ('atlsgm', 'Red_L'),
        ('atlsg', 'Red_L'),
        ('atlasusr', 'Red_L'),
        ('atlass', 'Red_L'),
        ('laspt', 'Red_L'),
        ('atlpilot', 'Red_L'),
        ('atpilot', 'Red_L'),
        ('iatpilot', 'Red_L'),
        ('atlasplt', 'Red_L'),
        ('atlaspt', 'Red_L'),
        ('atlaspil', 'Red_L'),
        ('atlasplot', 'Red_L'),
        ('atlplot', 'Red_L'),
        ('atlpil', 'Red_L'),
        ('atlpl', 'Red_L'),
        ('atlaspilot', 'Red_L'),
        ('atlprod', 'Red'),
        ('atlasger', 'Red'),
        ('atlasde', 'Red'),
        ('datlas', 'Red'),
        ('atlasit', 'Red'),
        ('atlde', 'Red'),
        ('atlit', 'Red'),
        ('atlasprod', 'Red'),
        ('atlasprd', 'Red'),
        ('atlsprd', 'Red'),
        ('atlprd', 'Red'),
        ('atlpr', 'Red'),
        ('iatlas', 'Red'),
        ('iatprd', 'Red'),
        ('iatl', 'Red'),
        ('aatlpd', 'Red'),
        ('atlasfx', 'Red'),
        ('atlastw', 'Red'),
        ('atlx', 'Red'),
        ('atlp', 'Red'),
        ('atlu', 'Red'),
        ('atlhs', 'Red'),
        ('atlashs', 'Red'),
        ('atlasp', 'Red'),
        ('atlasfr', 'Red'),
        ('atlasana', 'Red'),
        ('Eatlas', 'Red'),
        ('shatlas', 'Red'),
        ('lcgatlas', 'Red'),
        ('atlasL', 'Red'),
        ('atlasil', 'Red'),
        ('atlanaly', 'Red'),
        ('atlas', 'Red'),
        ('atlbr', 'Red'),
        ('atls', 'Red'),
        ('atl', 'Red'),
        ('atfx', 'Red'),
        ('atprd', 'Red'),
        ('atcanpu', 'Red'),
        ('atcanpt', 'Red_L'),
        ('atcan', 'Red'),
        ('atcpu', 'Red'),
        ('atsgm', 'Red_L'),
        ('pilatlas', 'Red_L'),
        ('pilatl', 'Red_L'),
        ('zipilatl', 'Red_L'),
        ('patlit', 'Red_L'),
        ('platl', 'Red_L'),
        ('pltatlas', 'Red_L'),
        ('pltatl', 'Red_L'),
        ('atplt', 'Red_L'),
        ('atlplt', 'Red_L'),
        ('piatlas', 'Red_L'),
        ('piatla', 'Red_L'),
        ('piatl', 'Red_L'),
        ('sgmatl', 'Red_L'),
        ('zisgmatl', 'Red_L'),
        #( sgmatl, 'Red'),
        ('prdatlas', 'Red'),
        ('prdatl', 'Red'),
        ('prdat', 'Red'),
        ('ziprdatl', 'Red'),
        ('ziatlas', 'Red'),
        ('patls', 'Red'),
        ('patlit', 'Red'),
        ('patl', 'Red'),
        ('nordugrid-atlas', 'Red'),
        ('nlv', 'Red_L'),
        ('ncfk', 'Green_L'),
        ('usatlas', 'Red'),
        #( CMS VO commonly found pool account names)
        ('cmssgm', 'Green_L'),
        ('cmsplt', 'Green_L'),
        ('pltcms', 'Green_L'),
        ('cmspilot', 'Green_L'),
        ('cmspil', 'Green_L'),
        ('pilcms', 'Green_L'),
        ('pcms', 'Green_L'),
        ('sgmcms', 'Green_L'),
        ('sgmcm', 'Green_L'),
        ('scms', 'Green_L'),
        ('priocms', 'Green_L'),
        ('cmsprio', 'Green_L'),
        ('pricms', 'Green_L'),
        ('cmsprod', 'Green'),
        ('cmsprd', 'Green'),
        ('cmsmcp', 'Green'),
        ('cmsnu', 'Green'),
        ('cmst1prd', 'Green'),
        ('cmprd', 'Green'),
        ('uscmsPool', 'Green'),
        ('uscms', 'Green'),
        ('cmsp', 'Green'),
        ('cmsusr', 'Green'),
        ('cmsuwu', 'Green'),
        ('cmsana', 'Green'),
        ('cmsger', 'Green'),
        ('cmss', 'Green'),
        ('cmszu', 'Green'),
        ('cmsau', 'Green'),
        ('twcms', 'Green'),
        ('cmsmu', 'Green'),
        ('dcms', 'Green'),
        ('prdcms', 'Green'),
        ('icms', 'Green'),
        ('cms', 'Green'),
        #( ALICE VO commonly found pool account name)s
        ('alicesgm', 'Cyan'),
        ('alice', 'Cyan'),
        ('alisc', 'Cyan'),
        ('alisgm', 'Cyan'),
        ('alisg', 'Cyan'),
        ('alibs', 'Cyan'),
        ('alis', 'Cyan'),
        ('alikn', 'Cyan'),
        ('ali', 'Cyan'),
        ('ialice', 'Cyan'),
        ('salice', 'Cyan'),
        ('sali', 'Cyan'),
        ('caliceuser', 'Cyan'),
        ('caliceusr', 'Cyan'),
        ('calice', 'Cyan'),
        ('calic', 'Cyan'),
        ('sgmalice', 'Cyan'),
        ('sgmali', 'Cyan'),
        #( LHCb VO commonly found pool account names)
        ('pdlhcb', 'Pink'),
        ('prdlhcb', 'Pink'),
        ('prdlhb', 'Pink'),
        ('prdlhc', 'Pink'),
        ('lhcbprd', 'Pink'),
        ('lhbprd', 'Pink'),
        ('lhprd', 'Pink'),
        ('ilhcb', 'Pink'),
        ('lhcbsgm', 'Purple'),
        ('lhcbs', 'Purple'),
        ('sgmlhcb', 'Purple'),
        ('sgmlhb', 'Purple'),
        ('sgmlhc', 'Purple'),
        ('lhcbplt', 'Purple'),
        ('lhcbpilot', 'Purple'),
        ('lhpilot', 'Purple'),
        ('lhcpilot', 'Purple'),
        ('lhcbpil', 'Purple'),
        ('lhbpil', 'Purple'),
        ('pillhcb', 'Purple'),
        ('plhcb', 'Purple'),
        ('pilhcb', 'Purple'),
        ('pltlhcb', 'Purple'),
        ('pillhb', 'Purple'),
        ('pllhc', 'Purple'),
        ('tlhcb', 'Pink'),
        ('lhcbhs', 'Pink'),
        ('lhcbp', 'Pink'),
        ('lhcb', 'Pink'),
        ('lhcp', 'Pink'),
        #( dteam VO commonly found pool account name)s
        ('dteamsgm', 'Brown'),
        ('dteamprd', 'Brown'),
        ('dteamuser', 'Brown'),
        ('dteamusr', 'Brown'),
        ('dteam', 'Brown'),
        ('dte', 'Brown'),
        #( OPS VO commonly found pool account names)
        ('opsplt', 'Yellow'),
        ('opsusr', 'Yellow'),
        ('opssgm', 'Yellow'),
        ('opssg', 'Yellow'),
        ('opsgm', 'Yellow'),
        ('sgmops', 'Yellow'),
        ('zisgmops', 'Yellow'),
        ('opsprd', 'Yellow'),
        ('opspil', 'Yellow'),
        ('pilops', 'Yellow'),
        ('samgrid', 'Yellow'),
        ('opss', 'Yellow'),
        ('sops', 'Yellow'),
        ('opsiber', 'Yellow'),
        ('opsib', 'Yellow'),
        ('ops', 'Yellow'),
        #( Other VOs from the EGEE-I,II,III era)
        ('egee', 'Blue_L'),
        #( Biomed VO)
        ('biomedusr', 'Blue_L'),
        ('biomed', 'Blue_L'),
        ('biomd', 'Blue_L'),
        ('biome', 'Blue_L'),
        ('biocw', 'Blue_L'),
        ('biostats', 'Blue_L'),
        ('biotech', 'Blue_L'),
        ('bio', 'Blue_L'),
        #( Gear V)O
        ('gearsgm', 'Blue_L'),
        ('gearprd', 'Blue_L'),
        ('gear', 'Blue_L'),
        #( DECH V)O
        ('dechsgm', 'Blue_L'),
        ('dechprd', 'Blue_L'),
        ('dechusr', 'Blue_L'),
        ('dech', 'Blue_L'),
        #( SEE V)O
        ('seeops', 'Blue_L'),
        ('seops', 'Blue_L'),
        ('seegrid', 'Blue_L'),
        ('seevo', 'Blue_L'),
        ('see', 'Blue_L'),
        #( ESR V)O
        ('esrsgm', 'Blue_L'),
        ('esr', 'Blue_L'),
        ('earthscience', 'Blue_L'),
        #( Fusion, auvergrid, compchem, enmr, voce, gaussian, balticgrid),
        #( Digital Media VO)s
        ('fusionprd', 'Blue_L'),
        ('fusionsgm', 'Blue_L'),
        ('fusion', 'Blue_L'),
        ('fusio', 'Blue_L'),
        ('fusi', 'Blue_L'),
        ('fusn', 'Blue_L'),
        ('fus', 'Blue_L'),
        ('auvergrid', 'Blue_L'),
        ('enmr', 'Blue_L'),
        ('complex', 'Blue_L'),
        ('compchem', 'Blue_L'),
        ('compc', 'Blue_L'),
        ('compl', 'Blue_L'),
        ('cmplx', 'Blue_L'),
        ('vocesgm', 'Blue_L'),
        ('voceprd', 'Blue_L'),
        ('voce', 'Blue_L'),
        ('gaussian', 'Blue_L'),
        ('balticgrid', 'Blue_L'),
        ('digmedia', 'Blue_L'),
        ('dmedia', 'Blue_L'),
        #( Hone VO)
        ('prdhone', 'Cyan_L'),
        ('prdhne', 'Cyan_L'),
        ('prdhon', 'Cyan_L'),
        ('honecker', 'Cyan_L'),
        ('honeprd', 'Cyan_L'),
        ('honesgm', 'Cyan_L'),
        ('phone', 'Cyan_L'),
        ('hone', 'Cyan_L'),
        ('honp', 'Cyan_L'),
        #( Other (High Energy) Physics VOs)
        ('sixto', 'Cyan_L'),
        ('sixt', 'Cyan_L'),
        ('babaradm', 'Cyan_L'),
        ('babarpro', 'Cyan_L'),
        ('babar', 'Cyan_L'),
        ('pheno', 'Cyan_L'),
        ('dzerojim', 'Cyan_L'),
        ('dzero', 'Cyan_L'),
        ('dze', 'Cyan_L'),
        ('dzerqa', 'Cyan_L'),
        ('theophys_', 'Cyan_L'),
        ('theophys', 'Cyan_L'),
        ('zeususr', 'Cyan_L'),
        ('zeus', 'Cyan_L'),
        ('argo', 'Cyan_L'),
        ('ilcprd', 'Cyan_L'),
        ('ilcpr', 'Cyan_L'),
        ('ilcp', 'Cyan_L'),
        ('ilcusr', 'Cyan_L'),
        ('ilcger', 'Cyan_L'),
        ('ilc', 'Cyan_L'),
        ('prdilc', 'Cyan_L'),
        ('pilc', 'Cyan_L'),
        ('sgmilc', 'Cyan_L'),
        ('augersgm', 'Cyan_L'),
        ('augerprd', 'Cyan_L'),
        ('auger', 'Cyan_L'),
        ('augp', 'Cyan_L'),
        ('aug', 'Cyan_L'),
        ('chatlas', 'Cyan_L'),
        ('chcms', 'Cyan_L'),
        ('chlhcb', 'Cyan_L'),
        ('geant', 'Cyan_L'),
        ('lhcft', 'Cyan_L'),
        ('magic', 'Cyan_L'),
        ('scier', 'Cyan_L'),
        ('planck', 'Cyan_L'),
        ('kaust', 'Brown'),
        #( Extras; these are really randomly found user names; needed for screen)
        #( clarity while in color more)
        ('mwilli', 'Brown'),
        ('por', 'Blue'),
        ('dorisf', 'Cyan'),
        ('campoman', 'Brown'),
        ('gallet', 'Blue'),
        ('tlemmin', 'Cyan'),
        ('ls', 'Cyan'),
        ('train', 'Blue_L'),
        ('pkoro', 'Brown'),
        ('fotis', 'Blue'),
        ('astrelchenko', 'Cyan'),
        ('tchristoudias', 'Brown'),
        ('dashed', 'Gray_L'),
        ('purple', 'Purple'),
        ('Red', 'Red'),
        ('DGray', 'Gray_D'),
        ('Brown', 'Brown'),
        ('_', 'White'),
        ('#', 'Gray_D'),
        ('account_not_colored', 'reset'),
        ('NoPattern', 'White'),
        ('Pending', 'Yellow'),
    ]
)

color_to_code = {
    'Gray_D': '1;30',
    'Gray_L': '1;37',
    'White': '1;37',
    'Red': '0;31',
    'Red_L': '1;31',
    'Red_LOnGrayBG': '1;31;40',
    'Green': '0;32',
    'Green_L': '1;32',
    'Purple': '0;35',
    'PurpleOnGrayBG': '0;35;40',
    'Pink': '1;35',
    'Brown': '0;33',
    'Yellow': '1;33',
    'Cyan': '0;36',
    'Cyan_L': '1;36',
    'Blue': '0;34',
    'Blue_L': '1;34',
    'reset': '0',
    'GrayBG': ';40',
    'MaroonBG': ';41',
    'GreenBG': ';42',
    'GoldBG': ';43',
    'BlueBG': ';44',
    'MagentaBG': ';45',
    'CyanBG': ';46',
    'Gray2BG': ';47',
    '': '',
    'NOBG': '',
}

queue_to_color = OrderedDict(
    [
        ('Pending', 'Yellow'),
        ('whole', 'Purple'),
        (r'grid\d+M', 'Red_L'),
        ('dteam.*', 'Red_L'),
        ('alice', 'Red_L'),
        ('cta', 'Pink'),
        ('grid3000M', 'Purple'),
        ('grid500M', 'Pink'),
        ('grid1000M', 'Red_L'),
        ('grid2000M', 'Red'),
    ]
)

nodestate_to_color = OrderedDict(
    [
        ('hqw', 'PurpleOnGrayBG'),
        ('r', 'Blue'),
        ('d', 'Gray'),
        ('o', 'MaroonBG'),
    ]
)
