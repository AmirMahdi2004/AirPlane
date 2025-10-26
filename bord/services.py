from datetime import datetime, timedelta
from .models import *


class MaintenanceService:
    def __init__(self, form):
        self.form = form
        self.airplane = form.cleaned_data['airplane']
        self.Landings = form.cleaned_data['Landings']
        self.AircraftCycles = form.cleaned_data['AircraftCycles']
        self.AircraftFlightHours = form.cleaned_data['AircraftFlightHours']
        self.Sll = ServiceLifeLimited
        self.MP = MP
        self.flt = FltHrs

    def save_sll(self):
        models = self.Sll.objects.filter(airplane=self.airplane)
        for model in models:
            if model.impact == 'AircraftFlightHours':
                self.Sll.objects.filter(airplane=self.form.cleaned_data['airplane'],No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.AircraftFlightHours,
                    RDays=model.NDDate - timedelta(self.AircraftFlightHours),
                    RACCycle=model.NDACCycle - self.AircraftFlightHours,
                    RLDNG=model.NDLDNG - self.AircraftFlightHours,
                    RENC=int(model.NDENC) - int(self.AircraftFlightHours),
                )
            elif model.impact == 'AircraftCycles':
                self.Sll.objects.filter(airplane=self.form.cleaned_data['airplane'],No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.AircraftFlightHours,
                    RDays=model.NDDate + timedelta(self.AircraftFlightHours),
                    RACCycle=model.NDACCycle - self.AircraftFlightHours,
                    RLDNG=model.NDLDNG - self.AircraftFlightHours,
                    RENC=int(model.NDENC) - int(self.AircraftFlightHours),
                )
            elif model.impact == 'Landings':
                self.Sll.objects.filter(airplane=self.form.cleaned_data['airplane'],No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.Landings,
                    RDays=model.NDDate - timedelta(self.Landings),
                    RACCycle=model.NDACCycle - self.Landings,
                    RLDNG=model.NDLDNG - self.Landings,
                    RENC=int(model.NDENC) - int(self.Landings),
                )
            # ServiceLifeLimited.objects.filter(airplane=self.airplane, No=model.No).update(
            #     NDACTime=NDACTime,
            #     NDDate=NDDate,
            #     NDACCycle=NDACCycle,
            #     NDLDNG=NDLDNG,
            #     NDENC=NDENC,
            #     RHours=RHours, RDays=RDays,
            #     RACCycle=RACCycle, RLDNG=RLDNG, RENC=RENC)

            print("two", model.No, model.impact, model.RLDNG)

        #             NDATIME_closed = LTTime + LDTime
        #             NDATI_closed = LDDate_time + timedelta(LTTime)
        #             NDACCycle_closed = LDACCycle + LTACCycle
        #             NDLDNG_closed = LDLDNG + LTLDNG
        #             NDENC_closed = LDENC + LTDENC
        #             RHours_closed = NDACTime - self.AircraftFlightHours
        #             RDays_closed = NDDate_time - timedelta(self.AircraftFlightHours)
        #             RACCycle_closed = NDACCycle - self.AircraftFlightHours
        #             RLDNG_closed = NDLDNG - self.AircraftFlightHours
        #             RENC_closed = int(NDENC) - int(self.AircraftFlightHours)

    def save_flt(self):
        models = self.flt.objects.filter(airplane=self.airplane)
        for model in models:
            if model.impact == 'AircraftFlightHours':
                self.flt.objects.filter(airplane=self.form.cleaned_data['airplane'], No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.AircraftFlightHours,
                    RDays=model.NDDate - timedelta(self.AircraftFlightHours),
                    RACCycle=model.NDACCycle - self.AircraftFlightHours,
                    RLDNG=model.NDLDNG - self.AircraftFlightHours,
                    RENC=int(model.NDENC) - int(self.AircraftFlightHours),
                )
            elif model.impact == 'AircraftCycles':
                self.flt.objects.filter(airplane=self.form.cleaned_data['airplane'], No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.AircraftFlightHours,
                    RDays=model.NDDate + timedelta(self.AircraftFlightHours),
                    RACCycle=model.NDACCycle - self.AircraftFlightHours,
                    RLDNG=model.NDLDNG - self.AircraftFlightHours,
                    RENC=int(model.NDENC) - int(self.AircraftFlightHours),
                )
            elif model.impact == 'Landings':
                self.flt.objects.filter(airplane=self.form.cleaned_data['airplane'], No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.Landings,
                    RDays=model.NDDate - timedelta(self.Landings),
                    RACCycle=model.NDACCycle - self.Landings,
                    RLDNG=model.NDLDNG - self.Landings,
                    RENC=int(model.NDENC) - int(self.Landings),
                )

    def save_mp(self):
        models = self.MP.objects.filter(airplane=self.airplane)
        for model in models:
            if model.impact == 'AircraftFlightHours':
                self.MP.objects.filter(airplane=self.form.cleaned_data['airplane'], No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.AircraftFlightHours,
                    RDays=model.NDDate - timedelta(self.AircraftFlightHours),
                    RACCycle=model.NDACCycle - self.AircraftFlightHours,
                    RLDNG=model.NDLDNG - self.AircraftFlightHours,
                    RENC=int(model.NDENC) - int(self.AircraftFlightHours),
                )
            elif model.impact == 'AircraftCycles':
                self.MP.objects.filter(airplane=self.form.cleaned_data['airplane'], No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.AircraftFlightHours,
                    RDays=model.NDDate + timedelta(self.AircraftFlightHours),
                    RACCycle=model.NDACCycle - self.AircraftFlightHours,
                    RLDNG=model.NDLDNG - self.AircraftFlightHours,
                    RENC=int(model.NDENC) - int(self.AircraftFlightHours),
                )
            elif model.impact == 'Landings':
                self.MP.objects.filter(airplane=self.form.cleaned_data['airplane'], No=model.No).update(
                    NDACTime=model.LTTime + model.LDTime,
                    NDDate=model.LDDate + timedelta(model.LTTime),
                    NDACCycle=model.LDACCycle + model.LTACCycle,
                    NDLDNG=model.LDLDNG + model.LTLDNG,
                    NDENC=model.LDENC + model.LTENC,
                    RHours=model.NDACTime - self.Landings,
                    RDays=model.NDDate - timedelta(self.Landings),
                    RACCycle=model.NDACCycle - self.Landings,
                    RLDNG=model.NDLDNG - self.Landings,
                    RENC=int(model.NDENC) - int(self.Landings),
                )

    #     def time_until_replacement_sll(self, impact,
    #                                    LDTime, LDDate, LDACCycle, LDLDNG, LDENC,
    #                                    LTTime, LTDate, LTACCycle, LTLDNG, LTDENC,
    #                                    NDACTime, NDDate, NDACCycle, NDLDNG, NDENC, ):
    #         LDDate_time = datetime.combine(LDDate, datetime.min.time())
    #         LTDate_time = datetime.combine(LTDate, datetime.min.time())
    #         NDDate_time = datetime.combine(NDDate, datetime.min.time())
    #
    #         if impact == 'AircraftFlightHours':
    #             NDATIME_closed = LTTime + LDTime
    #             NDATI_closed = LDDate_time + timedelta(LTTime)
    #             NDACCycle_closed = LDACCycle + LTACCycle
    #             NDLDNG_closed = LDLDNG + LTLDNG
    #             NDENC_closed = LDENC + LTDENC
    #             RHours_closed = NDACTime - self.AircraftFlightHours
    #             RDays_closed = NDDate_time - timedelta(self.AircraftFlightHours)
    #             RACCycle_closed = NDACCycle - self.AircraftFlightHours
    #             RLDNG_closed = NDLDNG - self.AircraftFlightHours
    #             RENC_closed = int(NDENC) - int(self.AircraftFlightHours)
    #
    #             return [NDATIME_closed, NDATI_closed, NDACCycle_closed, NDLDNG_closed, NDENC_closed, RHours_closed,
    #                     RDays_closed, RACCycle_closed, RLDNG_closed, RENC_closed]
    #
    #         elif impact == 'AircraftCycles':
    #             NDATIME_closed = LTTime + LDTime
    #             NDATI_closed = LDDate_time + timedelta(LTTime)
    #             NDACCycle_closed = LDACCycle + LTACCycle
    #             NDLDNG_closed = LDLDNG + LTLDNG
    #             NDENC_closed = LDENC + LTDENC
    #             RHours_closed = NDACTime - self.AircraftCycles
    #             RDays_closed = NDDate_time - timedelta(self.AircraftCycles)
    #             RACCycle_closed = NDACCycle - self.AircraftCycles
    #             RLDNG_closed = NDLDNG - self.AircraftCycles
    #             RENC_closed = int(NDENC) - int(self.AircraftCycles)
    #
    #             return [NDATIME_closed, NDATI_closed, NDACCycle_closed, NDLDNG_closed, NDENC_closed, RHours_closed,
    #                     RDays_closed, RACCycle_closed, RLDNG_closed, RENC_closed]
    #
    #         elif impact == 'Landings':
    #             NDATIME_closed = LTTime + LDTime
    #             NDATI_closed = LDDate_time + timedelta(LTTime)
    #             NDACCycle_closed = LDACCycle + LTACCycle
    #             NDLDNG_closed = LDLDNG + LTLDNG
    #             NDENC_closed = LDENC + LTDENC
    #             RHours_closed = NDACTime - self.Landings
    #             RDays_closed = NDDate_time - timedelta(self.Landings)
    #             RACCycle_closed = NDACCycle - self.Landings
    #             RLDNG_closed = NDLDNG - self.Landings
    #             RENC_closed = int(NDENC) - int(self.Landings)
    #
    #             return [NDATIME_closed, NDATI_closed, NDACCycle_closed, NDLDNG_closed, NDENC_closed, RHours_closed,
    #                     RDays_closed, RACCycle_closed, RLDNG_closed, RENC_closed]
    #
    #     def time_until_replacement_mp(self):
    #         pass
    #
    #     def time_until_replacement_flt(self):
    #         pass
    #
    #
    # class CalculatorSaving:
    #     def __init__(self, form, calculator):
    #         self.form = form
    #         self.calculator = calculator
    #
    #     # Calculation of consumption
    #     def calculator(self, impact,
    #                    LDTime, LDDate, LDACCycle, LDLDNG, LDENC,
    #                    LTTime, LTDate, LTACCycle, LTLDNG, LTDENC,
    #                    NDACTime, NDDate, NDACCycle, NDLDNG, NDENC, ):
    #         closed = MaintenanceService(self.form.cleaned_data['airplane'], self.form.cleaned_data['AircraftFlightHours'],
    #                                     self.form.cleaned_data['AircraftCycles'],
    #                                     self.form.cleaned_data['Landings']).time_until_replacement_sll(impact,
    #                                                                                                    LDTime, LDDate,
    #                                                                                                    LDACCycle,
    #                                                                                                    LDLDNG,
    #                                                                                                    LDENC,
    #                                                                                                    LTTime, LTDate,
    #                                                                                                    LTACCycle,
    #                                                                                                    LTLDNG,
    #                                                                                                    LTDENC,
    #                                                                                                    NDACTime, NDDate,
    #                                                                                                    NDACCycle,
    #                                                                                                    NDLDNG,
    #                                                                                                    NDENC, )
    #         return closed
    #
    #     # update data base
    #     def updating_sll(self, form):
    #         model = ServiceLifeLimited.objects.filter(airplane=form.cleaned_data['airplane'])
    #         for i in model:
    #             closed = self.calculator(form, i.impact, i.LDTime, i.LDDate, i.LDACCycle, i.LDLDNG,
    #                                      i.LDENC, i.LTTime, i.LTDate, i.LTACCycle, i.LTLDNG, i.LTENC,
    #                                      i.NDACTime, i.NDDate, i.NDACCycle, i.NDLDNG, i.NDENC)
    #             print(closed)
    #             ServiceLifeLimited.objects.filter(airplane=form.cleaned_data['airplane'], No=i.No).update(
    #                 NDACTime=closed[0],
    #                 NDDate=closed[1],
    #                 NDACCycle=closed[2],
    #                 NDLDNG=closed[3],
    #                 NDENC=closed[4],
    #                 RHours=closed[5], RDays=closed[6],
    #                 RACCycle=closed[7], RLDNG=closed[8], RENC=closed[9])

    # def updating_mp(self, model):
    #     model = MP.objects.filter(airplane=self.form.cleaned_data['airplane'])
    #     for i in model:
    #         closed = calculator(self.form, i.impact, i.LDHours, i.LDDate, i.LDACCycle, i.LDLDNG,
    #                             i.LDENC, i.INTHours, i.INTDays, i.INTACCycle, i.INTLDNG, i.INTRENC,
    #                             i.NEACTime, i.NEDate, i.NEACCycle, i.NELDNG, i.NEENC)
    #         MP.objects.filter(airplane=self.form .cleaned_data['airplane'], No=i.No).update(
    #             NEACTime=closed[0],
    #             NEDate=closed[1],
    #             NEACCycle=closed[2],
    #             NELDNG=closed[3],
    #             NEENC=closed[4],
    #             REHours=closed[5], REDays=closed[6],
    #             REACCycle=closed[7], RELDNG=closed[8], REENC=closed[9])
    #
    # def updating_flt(self, model):
    #     model = MP.objects.filter(airplane=self.form.cleaned_data['airplane'])
    #     for i in model:
    #         closed = calculator(self.form, i.impact, i.LDHours, i.LDDate, i.LDACCycle, i.LDLDNG,
    #                             i.LDENC, i.INTHours, i.INTDays, i.INTACCycle, i.INTLDNG, i.INTRENC,
    #                             i.NEACTime, i.NEDate, i.NEACCycle, i.NELDNG, i.NEENC)
    #         MP.objects.filter(airplane=self.form .cleaned_data['airplane'], No=i.No).update(
    #             NEACTime=closed[0],
    #             NEDate=closed[1],
    #             NEACCycle=closed[2],
    #             NELDNG=closed[3],
    #             NEENC=closed[4],
    #             REHours=closed[5], REDays=closed[6],
    #             REACCycle=closed[7], RELDNG=closed[8], REENC=closed[9])
