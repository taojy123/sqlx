import os
import execjs


def sqlformat(sql):
    # os.environ["EXECJS_RUNTIME"] = "Node"
    print('execjs:', execjs.get().name)
    js = open('sqlformat.js').read()
    ctx = execjs.compile(js)
    result = ctx.call('sqlformat', sql)
    return result



TESTSQL = """
SELECT
    id,
    mash_apply_mapping.unique_no,
    put_loan_borrowing_no AS loan_no,
    mash_apply_mapping.apply_no,
    'pro002' AS product_no,
    '借款成功' AS loan_status,
    NULL AS loan_fial_reason,
    put_loan_amount AS loan_money,
    put_loan_time AS create_time,
    mash_contract_no
FROM
    loan_data_inner.mf_ms_put_loan_account_check
LEFT JOIN (
    SELECT
        mash_contract_no,
        max(unique_no) AS unique_no,
        max(apply_no) AS apply_no
    FROM
        loan_front_manager.mf_business_apply
    GROUP BY
        mash_contract_no
) AS mash_apply_mapping ON mash_apply_mapping.mash_contract_no = mf_ms_put_loan_account_check.contract_no
WHERE
    unique_no IS NOT NULL
UNION ALL
    SELECT
        *, NULL AS mash_contract_no
    FROM
        loan_front_manager.mf_business_loan_apply_log
"""






print(sqlformat(TESTSQL))



