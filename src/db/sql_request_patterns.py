kkt_activated_true = '''
    select k.register_number_kkt,
           k.factory_number_fn,
           c.company_inn
    from kkt as k
             join company as c on k.company_id = c.id
    where k.activated = true
      and k.locked_no_payment = true
    limit 1;'''

kkt_activated_false = '''
    select k.register_number_kkt,
           k.factory_number_fn,
           c.company_inn
    from kkt as k
             join company as c on k.company_id = c.id
    where k.activated = false
    limit 1;'''