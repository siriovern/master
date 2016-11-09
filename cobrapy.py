__author__ = 'Siri'



import cobra.test


model = cobra.test.create_test_model(cobra.test.salmonella_pickle)
print len(model.reactions)
print len(model.metabolites)
print len(model.genes)

print '\n gene number 30 in gene list:'
print model.reactions[29]

print '\n item with id "atp_c" is:'
atp_c = model.metabolites.get_by_id("atp_c")
print atp_c.formula

print model


#for i in model.reactions:
#    print 'Reaction is: %s' % (i)

print model.reactions[1]
reaction = model.reactions.get_by_id('12DGR140tipp')
print '\nthe reaction is:\n %s' % reaction.reaction
print '\nthe name of the reaction:\n %s' % reaction.name

name1 = model.metabolites.get_by_id('12dgr140_p')
name2 = model.metabolites.get_by_id('12dgr140_c')
print '\nwith words:\n %s --> %s' % (name1.name, name2.name)
print '\nwith formula:\n %s --> %s' % (name1.formula, name2.formula)

model.optimize()
print model.solution
print model.solution.status

print '\n'
print model.summary()
print model.metabolites.glyc_e.summary()





